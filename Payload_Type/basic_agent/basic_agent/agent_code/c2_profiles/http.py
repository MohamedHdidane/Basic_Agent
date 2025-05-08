import requests
import base64

class HTTPC2Profile:
    def __init__(self, server="http://127.0.0.1:8080"):
        self.server = server
        self.checkin_endpoint = "/checkin"
        self.task_endpoint = "/tasks"
        self.response_endpoint = "/response"

    def checkin(self, payload):
        """Send checkin request to Mythic server."""
        try:
            response = requests.post(f"{self.server}{self.checkin_endpoint}", json=payload)
            if response.status_code == 200:
                return response.json()
            print(f"HTTP Checkin failed: {response.status_code}")
            return None
        except Exception as e:
            print(f"HTTP Checkin error: {e}")
            return None

    def get_task(self, task_id):
        """Fetch task from Mythic server."""
        try:
            response = requests.get(f"{self.server}{self.task_endpoint}/{task_id}")
            if response.status_code == 200:
                return response.json()
            print(f"HTTP Task fetch failed: {response.status_code}")
            return None
        except Exception as e:
            print(f"HTTP Task fetch error: {e}")
            return None

    def send_response(self, task_id, output):
        """Send response back to Mythic server."""
        response = {
            "task_id": task_id,
            "output": base64.b64encode(output.encode()).decode()
        }
        try:
            requests.post(f"{self.server}{self.response_endpoint}", json=response)
        except Exception as e:
            print(f"HTTP Response send error: {e}")