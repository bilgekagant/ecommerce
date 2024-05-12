from flask import Blueprint

accounting_bp = Blueprint('accounting', __name__)

@accounting_bp.route('/')
def index():
    return "Welcome to the Accounting Service"

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db, User
import uuid

@accounting_bp.route('/users', methods=['POST'])
def register_user():
    data = request.get_json()
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already registered'}), 409
    user = User(email=data['email'], username=data['username'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'user_id': user.user_id, 'username': user.username, 'email': user.email}), 20

@accounting_bp.route('/users/login', methods=['POST'])
def login_user():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and user.check_password(data['password']):
        return jsonify({'message': 'Login successful', 'user_id': user.user_id}), 200
    return jsonify({'message': 'Invalid email or password'}), 401
