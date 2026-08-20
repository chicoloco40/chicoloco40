import json
from os import environ as env
from urllib.parse import urlparse

from auth0_server_python.auth_server.server_client import ServerClient
from auth0_server_python.auth_types import LogoutOptions, StartInteractiveLoginOptions, StateData, TransactionData
from auth0_server_python.store.abstract import AbstractDataStore
from dotenv import load_dotenv
from flask import Flask, after_this_request, redirect, request, jsonify
from markupsafe import escape

load_dotenv()

app = Flask(__name__)

# Security Cookie Store Configuration
class CookieStore(AbstractDataStore):
    def __init__(self, secret, cookie_name, max_age, model):
        super().__init__({"secret": secret})
        self.cookie_name = cookie_name
        self.max_age = max_age
        self.model = model

    async def set(self, identifier, state, **_):
        @after_this_request
        def apply(response):
            data = state.model_dump() if hasattr(state, "model_dump") else state
            response.set_cookie(
                self.cookie_name,
                self.encrypt(identifier, data),
                httponly=True,
                samesite="Lax",
                secure=not env.get("APP_BASE_URL", "").startswith("http://"),
                max_age=self.max_age,
            )
            return response

    async def get(self, identifier, options=None):
        try:
            encrypted = options["request"].cookies.get(self.cookie_name)
            return self.model.model_validate(self.decrypt(identifier, encrypted)) if encrypted else None
        except Exception:
            app.logger.warning("Failed to decrypt cookie %s", self.cookie_name, exc_info=True)
            return None

    async def delete(self, *_, **__):
        @after_this_request
        def apply(response):
            response.delete_cookie(self.cookie_name)
            return response


def auth0():
    session_secret = env.get("AUTH0_SECRET")
    return ServerClient(
        domain=env.get("AUTH0_DOMAIN"),
        client_id=env.get("AUTH0_CLIENT_ID"),
        client_secret=env.get("AUTH0_CLIENT_SECRET"),
        redirect_uri=env.get("APP_BASE_URL") + "/callback",
        authorization_params={"scope": "openid profile email"},
        secret=session_secret,
        state_store=CookieStore(session_secret, "_a0_session", 259200, StateData),  # 3 days
        transaction_store=CookieStore(session_secret, "_a0_tx", 300, TransactionData),  # 5 min
    )


# --- WEB DASHBOARD ROUTES ---

@app.route("/")
async def home():
    user = await auth0().get_user({"request": request})
    head = "<!DOCTYPE html><title>CL40 World Control Panel</title>"

    if user:
        return f"""
            {head}
            <p>Logged in as {escape(user.get("email", ""))}</p>
            <h1>User Profile Dashboard</h1>
            <pre>{escape(json.dumps(user, indent=2))}</pre>
            <hr>
            <p>Your API Status: <strong>Active Secure Guardian</strong></p>
            <a href="/logout">Logout</a>
        """

    return f"""
        {head}
        <h1>Welcome to CL40 World Application Gateway</h1>
        <a href="/login?screen_hint=signup">Signup</a> | 
        <a href="/login">Login</a>
    """


@app.route("/login")
async def login():
    url = await auth0().start_interactive_login(
        options=StartInteractiveLoginOptions(
            authorization_params=dict(request.args),
        ),
        store_options={"request": request},
    )
    return redirect(url)


@app.route("/callback")
async def callback():
    try:
        await auth0().complete_interactive_login(
            url=request.url, store_options={"request": request},
        )
        return redirect("/")
    except Exception:
        app.logger.exception("Callback error")
        return "Something went wrong. Check server logs for details.", 400


@app.route("/logout")
async def logout():
    url = await auth0().logout(
        options=LogoutOptions(return_to=env.get("APP_BASE_URL")),
        store_options={"request": request},
    )
    return redirect(url)


# --- NEW CUSTOM SECURE API ENDPOINTS FOR CHANNELS/BOTS ---

@app.route("/api/user/profile", methods=["GET"])
async def api_get_profile():
    """Secure endpoint for checking your developer channel profile data via JSON."""
    user = await auth0().get_user({"request": request})
    if not user:
        return jsonify({"error": "Unauthorized Access Request", "status": 401}), 401
    return jsonify({"status": "Authorized", "user_data": user})


@app.route("/api/system/status", methods=["GET"])
def api_system_status():
    """Public system heart-beat or status check."""
    return jsonify({
        "application": "CL40 World",
        "guardian_network": "Active",
        "api_gateway": "Online"
    })


if __name__ == "__main__":
    url = urlparse(env.get("APP_BASE_URL"))
    app.run(host=url.hostname or "0.0.0.0", port=url.port or 5000)
