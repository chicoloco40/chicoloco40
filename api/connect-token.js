module.exports = async (req, res) => {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "POST only" });
  }

  const { PIPEDREAM_CLIENT_ID, PIPEDREAM_CLIENT_SECRET, PIPEDREAM_PROJECT_ID } = process.env;
  const environment = process.env.PIPEDREAM_ENVIRONMENT || "production";

  if (!PIPEDREAM_CLIENT_ID || !PIPEDREAM_CLIENT_SECRET || !PIPEDREAM_PROJECT_ID) {
    return res.status(500).json({ error: "Missing Pipedream environment variables" });
  }

  const userId = (req.body && req.body.external_user_id) || "";
  if (!/^[A-Za-z0-9_-]{8,64}$/.test(userId)) {
    return res.status(400).json({ error: "Invalid external_user_id" });
  }

  try {
    const oauthRes = await fetch("https://api.pipedream.com/v1/oauth/token", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        grant_type: "client_credentials",
        client_id: PIPEDREAM_CLIENT_ID,
        client_secret: PIPEDREAM_CLIENT_SECRET,
        scope: "connect:tokens:create",
      }),
    });
    if (!oauthRes.ok) {
      return res.status(502).json({ error: "Pipedream OAuth failed", status: oauthRes.status });
    }
    const { access_token } = await oauthRes.json();

    const tokenRes = await fetch(
      "https://api.pipedream.com/v1/connect/" + PIPEDREAM_PROJECT_ID + "/tokens",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer " + access_token,
          "x-pd-environment": environment,
        },
        body: JSON.stringify({
          external_user_id: userId,
          project_id: PIPEDREAM_PROJECT_ID,
        }),
      }
    );
    if (!tokenRes.ok) {
      return res.status(502).json({ error: "Connect token failed", status: tokenRes.status });
    }
    const data = await tokenRes.json();

    return res.status(200).json({
      url: data.connect_link_url,
      expires_at: data.expires_at,
    });
  } catch (err) {
    return res.status(500).json({ error: "Server error" });
  }
};
