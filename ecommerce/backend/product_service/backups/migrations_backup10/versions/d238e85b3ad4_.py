"""empty message

Revision ID: d238e85b3ad4
Revises: 
Create Date: 2024-05-21 00:14:01.693058

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import uuid


# revision identifiers, used by Alembic.
revision: str = 'd238e85b3ad4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


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
