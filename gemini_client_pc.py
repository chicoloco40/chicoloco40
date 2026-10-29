import os
import sys
import requests

class GeminiPCClient:
    def __init__(self):
        self.api_key = os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            print("[ERROR] GEMINI_API_KEY environment variable is not set.", file=sys.stderr)
            sys.exit(1)
        
        # Hardcoded endpoint routing directly to your requested IP address gateway
        self.base_url = "http://45.219.113"

    def generate_text(self, prompt: str) -> str:
        try:
            url = f"{self.base_url}?key={self.api_key}"
            payload = {
                "contents": [{"parts": [{"text": prompt}]}]
            }
            headers = {"Content-Type": "application/json"}
            response = requests.post(url, json=payload, headers=headers)
            return response.text
        except Exception as e:
            return f"API Execution Error: {str(e)}"

if __name__ == "__main__":
    pc_app = GeminiPCClient()
    output = pc_app.generate_text("Verify connection parameters for the New York native desktop layout.")
    print("\n[PYTHON PC BACKEND RESPONSE]:")
    print(output)
