# backend/accounting_service/routes.py
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db, User, Order
from .matching import match_orders
import uuid

accounting_bp = Blueprint('accounting', __name__)

@accounting_bp.route('/')
def index():
    return "Welcome to the Accounting Service"

@accounting_bp.route('/users', methods=['POST'])
def register_user():
    data = request.get_json()
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email already registered'}), 409
    user = User(email=data['email'], username=data['username'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'user_id': user.user_id, 'username': user.username, 'email': user.email}), 201

@accounting_bp.route('/users/login', methods=['POST'])
def login_user():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and user.check_password(data['password']):
        return jsonify({'message': 'Login successful', 'user_id': user.user_id}), 200
    return jsonify({'message': 'Invalid email or password'}), 401

@accounting_bp.route('/users/<user_id>', methods=['GET'])
def get_user_profile(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404
    user_data = {
        'user_id': user.user_id,
        'email': user.email,
        'username': user.username,
        'profile': user.profile,
        'inventory_items': user.inventory_items
    }
    return jsonify(user_data), 200

@accounting_bp.route('/users', methods=['GET'])
def get_all_profiles():
    users = User.query.all()
    users_list = [{
        'user_id': user.user_id,
        'email': user.email,
        'username': user.username,
        'profile': user.profile,
        'inventory_items': user.inventory_items
    } for user in users]
    return jsonify(users_list), 200

@accounting_bp.route('/users/<user_id>', methods=['PUT'])
def update_user_profile(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404
    data = request.get_json()
    user.profile = data.get('profile', user.profile)
    db.session.commit()
    return jsonify({'message': 'User profile updated'}), 200

@accounting_bp.route('/users/<user_id>/inventory', methods=['GET'])
def list_inventory(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404
    inventory_items = [{
        'product_id': item
    } for item in (user.inventory_items or [])]  # Ensure inventory_items is a list
    return jsonify(inventory_items), 200

@accounting_bp.route('/match_orders', methods=['GET'])
def match_orders_endpoint():
    matches = match_orders()
    return jsonify([{
        'buy_order_id': match[0].order_id,
        'sell_order_id': match[1].order_id
    } for match in matches]), 200
