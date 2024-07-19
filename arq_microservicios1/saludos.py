from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greetings', methods=['GET'])
def get_greetings():
    greetings = [
        {"id": 1, "texto": "Hola!"},
        {"id": 2, "texto": "Salud!"},
    ]
    return jsonify(greetings)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
