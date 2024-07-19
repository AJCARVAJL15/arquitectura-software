from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/messages', methods=['GET'])
def get_messages():
    messages = [
        {"id": 1, "texto": "Hola!"},
        {"id": 2, "texto": "estudiante"},
    ]
    return jsonify(messages)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
