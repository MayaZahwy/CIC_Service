from flask import Flask, jsonify
from datetime import datetime
app = Flask(__name__)
@app.route('/api/python', methods=['GET'])
def get_data():
    return jsonify({
        "message": "Hello from Python Flask Service!",
        "timestamp": datetime.utcnow().isoformat()
    })
if __name__ == '__main__':
    # Running on port 5002
    app.run(host='0.0.0.0', port=5002)