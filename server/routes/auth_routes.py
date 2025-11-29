from flask import Blueprint, request, session, jsonify
from config import db
from models import User

auth_bp = Blueprint('auth_bp', __name__)

# Create a new user + auto-login
@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"error": "Username already taken"}), 409

    new_user = User(username=username)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    # Save user login state
    session['user_id'] = new_user.id

    return jsonify({"id": new_user.id, "username": new_user.username}), 201

# Login existing user
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid credentials"}), 401

    session['user_id'] = user.id

    return jsonify({"id": user.id, "username": user.username}), 200

# Check if user is logged in

@auth_bp.route('/check_session', methods=['GET'])
def check_session():
    user_id = session.get('user_id')

    if not user_id:
        return jsonify({"error": "Not logged in"}), 401

    user = User.query.get(user_id)
    return jsonify({"id": user.id, "username": user.username}), 200

# Logout user
@auth_bp.route('/logout', methods=['DELETE'])
def logout():
    session.pop('user_id', None)
    return '', 204
