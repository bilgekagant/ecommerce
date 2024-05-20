"""empty message

Revision ID: 829cdeda4d6e
Revises: 
Create Date: 2024-05-19 18:00:07.751749

"""
# backend/accounting_service/migrations/versions/829cdeda4d6e_add_initial_tables.py
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import uuid

# revision identifiers, used by Alembic.
revision = '829cdeda4d6e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Create the enums first
    order_types = postgresql.ENUM('buy', 'sell', name='order_types')
    order_types.create(op.get_bind(), checkfirst=True)

    order_statuses = postgresql.ENUM('open', 'matched', 'closed', name='order_statuses')
    order_statuses.create(op.get_bind(), checkfirst=True)

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
        sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False, primary_key=True, default=uuid.uuid4),
        sa.Column('email', sa.String(length=120), nullable=False, unique=True),
        sa.Column('password_hash', sa.String(length=256), nullable=True),
        sa.Column('username', sa.String(length=80), nullable=False, unique=True),
        sa.Column('profile', postgresql.JSONB, nullable=True),
        sa.Column('inventory_items', postgresql.ARRAY(postgresql.UUID(as_uuid=True)), nullable=True)
    )

    op.create_table('transaction',
        sa.Column('id', sa.Integer, nullable=False, primary_key=True),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('amount', sa.Float, nullable=False),
        sa.Column('type', sa.String(length=20), nullable=False),
        sa.Column('timestamp', sa.DateTime, nullable=False)
    )

    op.create_table('order',
        sa.Column('order_id', postgresql.UUID(as_uuid=True), nullable=False, primary_key=True, default=uuid.uuid4),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('user.user_id'), nullable=False),
        sa.Column('order_type', sa.Enum('buy', 'sell', name='order_types'), nullable=False),
        sa.Column('product_details', postgresql.JSONB, nullable=True),
        sa.Column('price', sa.Numeric, nullable=True),
        sa.Column('status', sa.Enum('open', 'matched', 'closed', name='order_statuses'), nullable=False)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    op.drop_table('transaction')
    op.drop_table('user')

    # Drop the enums last
    order_types = postgresql.ENUM('buy', 'sell', name='order_types')
    order_types.drop(op.get_bind(), checkfirst=True)

    order_statuses = postgresql.ENUM('open', 'matched', 'closed', name='order_statuses')
    order_statuses.drop(op.get_bind(), checkfirst=True)
    # ### end Alembic commands ###
