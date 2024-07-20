from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greetings', methods=['GET'])
def get_greetings():
    greetings = [
        {"id": 1, "text": "Hola estoy aqui"},
        {"id": 2, "text": "saludos!"},
    ]
    return jsonify(greetings)

if __name__ == '__main__':
    app.run(port=5002)
