# server.py
from flask import Flask, request
import base64
import re
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def receive():
    ua = request.headers.get('User-Agent', '')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if ua:
        match = re.search(r'Steg-(.*?)\)', ua)
        if match:
            hidden = base64.b64decode(match.group(1)).decode()
            print(f"[{timestamp}] Hidden Data Received: {hidden}")
            return f"Data received: {hidden}", 200
    
    return "No stego data found.", 404

if __name__ == "__main__":
    app.run(debug=True)
