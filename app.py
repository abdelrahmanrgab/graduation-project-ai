from flask import Flask, request, jsonify
from flask_cors import CORS
from result import result
import pickle
import os

app = Flask(__name__)
CORS(app)  

@app.route('/')
def index():
    return "Hello!"

@app.route('/page', methods=['POST'])
def page_data():
    try:
        if not request.json or 'text' not in request.json:
            return jsonify({"error": "Invalid input"}), 400

        text = request.json['text']
        # result_data = result.process_text(text)
        return jsonify({"text": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    try:
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)
    except Exception as e:
        print("Error:", e)
