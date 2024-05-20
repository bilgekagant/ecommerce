# # products.routes
# from flask import Blueprint, request, jsonify
# from .models import db, Product

# product_bp = Blueprint('product', __name__)

# @product_bp.route('/', methods=['POST'])
# def create_product():
#     data = request.get_json()
#     product = Product(
#         name=data['name'],
#         brand=data['brand'],
#         model=data['model'],
#         year=data['year'],
#         condition=data['condition'],
#         images=data['images']
#     )
#     db.session.add(product)
#     db.session.commit()
#     return jsonify({'product_id': product.product_id}), 201

# @product_bp.route('/<product_id>', methods=['GET'])
# def get_product(product_id):
#     product = Product.query.get(product_id)
#     if not product:
#         return jsonify({'message': 'Product not found'}), 404
#     return jsonify({
#         'product_id': product.product_id,
#         'name': product.name,
#         'brand': product.brand,
#         'model': product.model,
#         'year': product.year,
#         'condition': product.condition,
#         'images': product.images
#     }), 200

# @product_bp.route('/', methods=['GET'])
# def get_all_products():
#     products = Product.query.all()
#     products_list = [{
#         'product_id': product.product_id,
#         'name': product.name,
#         'brand': product.brand,
#         'model': product.model,
#         'year': product.year,
#         'condition': product.condition,
#         'images': product.images
#     } for product in products]
#     return jsonify(products_list), 200  

# @product_bp.route('/<product_id>', methods=['PUT'])
# def update_product(product_id):
#     product = Product.query.get(product_id)
#     if not product:
#         return jsonify({'message': 'Product not found'}), 404
#     data = request.get_json()
#     product.name = data.get('name', product.name)
#     product.brand = data.get('brand', product.brand)
#     product.model = data.get('model', product.model)
#     product.year = data.get('year', product.year)
#     product.condition = data.get('condition', product.condition)
#     product.images = data.get('images', product.images)
#     db.session.commit()
#     return jsonify({'message': 'Product updated'}), 200

# @product_bp.route('/<product_id>', methods=['DELETE'])
# def delete_product(product_id):
#     product = Product.query.get(product_id)
#     if not product:
#         return jsonify({'message': 'Product not found'}), 404
#     db.session.delete(product)
#     db.session.commit()
#     return jsonify({'message': 'Product deleted'}), 200
# -----
# backend/product_service/routes.py
from flask import Blueprint, request, jsonify
from .models import db, Product
import uuid

product_bp = Blueprint('product', __name__)

@product_bp.route('/', methods=['POST'])
def create_product():
    data = request.get_json()
    product = Product(
        product_id=uuid.uuid4(),  # Generate a new UUID for the product_id
        name=data['name'],
        brand=data['brand'],
        model=data['model'],
        year=data['year'],
        condition=data['condition'],
        images=data['images']
    )
    db.session.add(product)
    db.session.commit()
    return jsonify({'product_id': product.product_id}), 201

@product_bp.route('/', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    products_list = [{
        'product_id': product.product_id,
        'name': product.name,
        'brand': product.brand,
        'model': product.model,
        'year': product.year,
        'condition': product.condition,
        'images': product.images
    } for product in products]
    return jsonify(products_list), 200

@product_bp.route('/<product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    return jsonify({
        'product_id': product.product_id,
        'name': product.name,
        'brand': product.brand,
        'model': product.model,
        'year': product.year,
        'condition': product.condition,
        'images': product.images
    }), 200

@product_bp.route('/<product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    data = request.get_json()
    product.name = data.get('name', product.name)
    product.brand = data.get('brand', product.brand)
    product.model = data.get('model', product.model)
    product.year = data.get('year', product.year)
    product.condition = data.get('condition', product.condition)
    product.images = data.get('images', product.images)
    db.session.commit()
    return jsonify({'message': 'Product updated'}), 200

@product_bp.route('/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted'}), 200
