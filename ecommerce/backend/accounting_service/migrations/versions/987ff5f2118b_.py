"""empty message

Revision ID: 987ff5f2118b
Revises: b70de4e6ff84
Create Date: 2024-05-20 21:57:35.476243

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import uuid

# revision identifiers, used by Alembic.
revision = '987ff5f2118b'
down_revision = 'b70de4e6ff84'
branch_labels = None
depends_on = None

# Define enum types
order_types = postgresql.ENUM('buy', 'sell', name='order_types', create_type=False)
order_statuses = postgresql.ENUM('open', 'matched', 'closed', name='order_statuses', create_type=False)

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    
    # Create enum types if they don't already exist
    if 'order_types' not in inspector.get_enums():
        order_types.create(bind)
    if 'order_statuses' not in inspector.get_enums():
        order_statuses.create(bind)

    # Create tables
    op.create_table('transaction',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('amount', sa.Float(), nullable=False),
        sa.Column('type', sa.String(length=20), nullable=False),
        sa.Column('timestamp', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
        sa.Column('user_id', sa.UUID(), nullable=False),
        sa.Column('email', sa.String(length=120), nullable=False),
        sa.Column('password_hash', sa.String(length=128), nullable=True),
        sa.Column('username', sa.String(length=80), nullable=False),
        sa.Column('profile', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column('inventory_items', sa.ARRAY(sa.UUID()), nullable=True),
        sa.PrimaryKeyConstraint('user_id'),
        sa.UniqueConstraint('email'),
        sa.UniqueConstraint('username')
    )
    op.create_table('order',
        sa.Column('order_id', sa.UUID(), nullable=False),
        sa.Column('user_id', sa.UUID(), nullable=False),
        sa.Column('order_types', postgresql.ENUM('buy', 'sell', name='order_types', create_type=False), nullable=True),
        sa.Column('product_details', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column('price', sa.Numeric(), nullable=True),
        sa.Column('status', postgresql.ENUM('open', 'matched', 'closed', name='order_statuses', create_type=False), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
        sa.PrimaryKeyConstraint('order_id')
    )
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    op.drop_table('user')
    op.drop_table('transaction')

    # Drop enum types if they exist
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    
    if 'order_types' in inspector.get_enums():
        order_types.drop(bind, checkfirst=False)
    if 'order_statuses' in inspector.get_enums():
        order_statuses.drop(bind, checkfirst=False)
    # ### end Alembic commands ###
