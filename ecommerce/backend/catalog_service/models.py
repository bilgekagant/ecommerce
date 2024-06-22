from extensions import db
from sqlalchemy.dialects.postgresql import UUID, JSONB
import uuid

class CatalogItem(db.Model):
    item_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = db.Column(UUID(as_uuid=True), db.ForeignKey('product.product_id'), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    attributes = db.Column(JSONB)

    def __repr__(self):
        return f'<CatalogItem {self.item_id}>'