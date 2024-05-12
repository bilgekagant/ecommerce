from main import db
import uuid
from sqlalchemy.dialects.postgresql import UUID, JSONB

class User(db.Model):
    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    username = db.Column(db.String(80), unique=True, nullable=False)
    profile = db.Column(JSONB)
    inventory_items = db.Column(db.ARRAY(UUID))

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
