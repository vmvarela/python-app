from datetime import datetime
from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route("/api/v3/details")
def details():
    return jsonify({
        "time": datetime.now().strftime("%I:%M:%S%p on %B %d, %Y"),
        "hostname": socket.gethostname(),
        "message": "Hola desde Flask API v3!"
    })

@app.route("/api/v3/healthz")
def healthz():
    return jsonify({"status": "up"}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)

# '/api/v1/details'
# '/api/v1/healthz'