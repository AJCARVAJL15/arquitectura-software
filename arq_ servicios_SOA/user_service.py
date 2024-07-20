from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route('/create_user', methods=['POST'])
def create_user():
    user_id = request.json.get('id')
    user_name = request.json.get('name')
    users[user_id] = user_name
    return jsonify({"message": "User created successfully", "user_id": user_id, "user_name": user_name}), 201

@app.route('/get_user/<user_id>', methods=['GET'])
def get_user(user_id):
    user_name = users.get(user_id)
    if user_name:
        return jsonify({"user_id": user_id, "user_name": user_name}), 200
    else:
        return jsonify({"message": "User not found"}), 404

if __name__ == '__main__':
    app.run(port=5000)
