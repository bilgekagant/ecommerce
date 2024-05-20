"""empty message

Revision ID: 309d7db74e98
Revises: 
Create Date: 2024-05-20 22:24:59.927568

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import uuid

# revision identifiers, used by Alembic.
revision = '309d7db74e98'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Create tables
    op.create_table('product',
        sa.Column('product_id', postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
        sa.Column('name', sa.String(length=80), nullable=False),
        sa.Column('brand', sa.String(length=80), nullable=False),
        sa.Column('model', sa.String(length=80), nullable=False),
        sa.Column('year', sa.Integer, nullable=False),
        sa.Column('condition', sa.String(length=80), nullable=False),
        sa.Column('images', postgresql.ARRAY(sa.String), nullable=True)
    )

def downgrade():
    # Drop the tables
    op.drop_table('product')