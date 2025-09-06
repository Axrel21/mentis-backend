
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt
from . import bcrypt

auth_blueprint = Blueprint('auth', __name__)

# In-memory user store (for demonstration purposes)
users = {}

@auth_blueprint.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users:
        return jsonify({"msg": "Username already exists"}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    users[username] = {"password": hashed_password}

    return jsonify({"msg": "User created"}), 201

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = users.get(username)

    if user and bcrypt.check_password_hash(user['password'], password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)

    return jsonify({"msg": "Bad username or password"}), 401

@auth_blueprint.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    # In a real application, you would add the token to a blacklist.
    # For this example, we'll just send a success message.
    jti = get_jwt()['jti']
    # In a real app, you would store this jti in a database or cache.
    return jsonify({"msg": "Successfully logged out"})


@auth_blueprint.route('/profile')
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
