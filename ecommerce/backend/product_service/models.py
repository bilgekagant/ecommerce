import uuid
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    product_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(255), nullable=False)
    brand = db.Column(db.String(100))
    model = db.Column(db.String(100))
    year = db.Column(db.Integer)
    condition = db.Column(db.String(100))
    images = db.Column(db.ARRAY(db.String))  # Array of image URLs

    def __repr__(self):
        return f'<Product {self.name}>'