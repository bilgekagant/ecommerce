# products.models
from extensions import db
from sqlalchemy.dialects.postgresql import UUID, JSONB, ARRAY
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()
metadata = Base.metadata

class Product(db.Model):
    product_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(80), nullable=False)
    brand = db.Column(db.String(80), nullable=False)
    model = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    condition = db.Column(db.String(80), nullable=False)
    images = db.Column(ARRAY(db.String), nullable=True)

    def __repr__(self):
        return f'<Product {self.name}>'


