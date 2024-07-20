from flask import Flask, request, jsonify

app = Flask(__name__)

credentials = {
    "user1": "password1",
    "user2": "password2"
}

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.json.get('username')
    password = request.json.get('password')
    if credentials.get(username) == password:
        return jsonify({"message": "Authentication successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(port=5001)
