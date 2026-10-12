import requests
import json

# Spotify Credentials
CLIENT_ID = "1510455630387740812"
CLIENT_SECRET = "PASTE_YOUR_ACTUAL_CLIENT_SECRET_HERE"
USER_ID = "31aohibriwhmd5qowjsgwfbkitwe"

def get_access_token(client_id, client_secret):
    """Generates an Access Token dynamically using Client Credentials Flow"""
    url = "https://accounts.spotify.com/api/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print(f"[ERROR] Failed to obtain token: {response.status_code} - {response.text}")
        return None

# Retrieve Access Token
ACCESS_TOKEN = get_access_token(CLIENT_ID, CLIENT_SECRET)

HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

def get_user_profile():
    """Fetch public profile details for the target user"""
    url = f"https://api.spotify.com/v1/users/{USER_ID}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"[ERROR] {response.status_code}: {response.text}")
        return None

if __name__ == "__main__":
    print("--- Spotify Engine Active ---")
    if ACCESS_TOKEN:
        profile = get_user_profile()
        if profile:
            print(f"User Profile Loaded: {profile.get('display_name')} ({profile.get('id')})")
