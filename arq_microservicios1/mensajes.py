from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/messages', methods=['GET'])
def get_messages():
    messages = [
        {"id": 1, "text": "Holaa"},
        {"id": 2, "text": "buenos dias"},
    ]
    return jsonify(messages)

if __name__ == '__main__':
    app.run(port=5001)
