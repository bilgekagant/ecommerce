from flask import Blueprint, request, jsonify
from .models import db, CatalogItem
import uuid

catalog_bp = Blueprint('catalog', __name__)

@catalog_bp.route('/')
def index():
    return "Welcome to the Catalog Service"

@catalog_bp.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    catalog_item = CatalogItem(
        product_id=data['product_id'],
        category=data['category'],
        attributes=data.get('attributes', {})
    )
    db.session.add(catalog_item)
    db.session.commit()
    return jsonify({'item_id': catalog_item.item_id, 'category': catalog_item.category}), 201

@catalog_bp.route('/categories/<category>', methods=['GET'])
def get_products_by_category(category):
    items = CatalogItem.query.filter_by(category=category).all()
    items_list = [{
        'item_id': item.item_id,
        'product_id': item.product_id,
        'category': item.category,
        'attributes': item.attributes
    } for item in items]
    return jsonify(items_list), 200

@catalog_bp.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('query')
    items = CatalogItem.query.filter(CatalogItem.attributes.contains({'name': query})).all()
    items_list = [{
        'item_id': item.item_id,
        'product_id': item.product_id,
        'category': item.category,
        'attributes': item.attributes
    } for item in items]
    return jsonify(items_list), 200

