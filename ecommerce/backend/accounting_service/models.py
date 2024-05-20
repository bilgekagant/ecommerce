# accounting.models

import uuid
from sqlalchemy.dialects.postgresql import UUID, JSONB, ARRAY
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(20), nullable=False)  # 'credit' or 'debit'
    timestamp = db.Column(db.DateTime, nullable=False)

class User(db.Model):
    user_id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256))  # Increase length to 256
    username = db.Column(db.String(80), unique=True, nullable=False)
    profile = db.Column(JSONB, nullable=True)
    inventory_items = db.Column(ARRAY(db.String(36)), nullable=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

class Order(db.Model):
    order_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.user_id'), nullable=False)
    order_type = db.Column(db.Enum('buy', 'sell', name='order_types'), nullable=False)
    product_details = db.Column(JSONB)
    price = db.Column(db.Numeric)
    status = db.Column(db.Enum('open', 'matched', 'closed', name='order_statuses'), nullable=False)

    def __repr__(self):
        return f'<Order {self.order_id}>'
