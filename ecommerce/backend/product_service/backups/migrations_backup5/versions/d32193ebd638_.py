"""initial migration

Revision ID: 70c8d44be996
Revises: ae79d65fe7d0
Create Date: 2024-05-18 19:31:39.196309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70c8d44be996'
down_revision = 'ae79d65fe7d0'
branch_labels = None
depends_on = None


def upgrade():
    bind = op.get_bind()
    inspector = sa.inspect(bind)

    # Create enum types if they don't already exist (if applicable)
    # if 'order_types' not in inspector.get_enums():
    #     order_types.create(bind)
    # if 'order_statuses' not in inspector.get_enums():
    #     order_statuses.create(bind)

    # Create tables
    op.create_table('product',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=80), nullable=False),
        sa.Column('brand', sa.String(length=80), nullable=False),
        sa.Column('model', sa.String(length=80), nullable=False),
        sa.Column('year', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('product')

    # Drop enum types (if applicable)
    # bind = op.get_bind()
    # inspector = sa.inspect(bind)
    
    # if 'order_types' in inspector.get_enums():
    #     order_types.drop(bind, checkfirst=True)
    # if 'order_statuses' in inspector.get_enums():
    #     order_statuses.drop(bind, checkfirst=True)