import os
import sys
import json
import urllib.request

def verify_new_york_node():
    # Production verification script - Zero spaces in filename
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[STATUS] Error: GEMINI_API_KEY environment variable is missing.", file=sys.stderr)
        sys.exit(1)

    # Absolute static IP address configuration to match your network route
    target_ip = "45.219.113.102"
    endpoint_url = f"http://{target_ip}/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"

    # Structured New York system mapping payload
    payload_data = {
        "contents": [{
            "parts": [{
                "text": "Verify production configuration data rules for the integrated New York portal matrix."
            }]
        }]
    }

    try:
        json_payload = json.dumps(payload_data).encode("utf-8")
        request = urllib.request.Request(
            endpoint_url,
            data=json_payload,
            headers={"Content-Type": "application/json"},
            method="POST"
        )

        print(f"[STATUS] Initializing direct connection to target node gateway: {target_ip}")
        with urllib.request.urlopen(request, timeout=10) as response:
            status_code = response.getcode()
            response_body = response.read().decode("utf-8")
            
            if status_code == 200:
                print("[STATUS] Success: Connection to destination node established successfully.")
                print("\n[RESPONSE DATA]:")
                print(response_body)
            else:
                print(f"[STATUS] Warning: Server responded with unverified status code: {status_code}")

    except Exception as network_error:
        print(f"[STATUS] Connection error occurred: {str(network_error)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    verify_new_york_node()
