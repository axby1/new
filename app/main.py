from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get("https://api.github.com")
    return jsonify({
        "message": "Hello from Flask!",
        "github_status": response.status_code
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
