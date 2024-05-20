"""empty message

Revision ID: 83401bb3e69d
Revises: 7f4c1ea6c8c0
Create Date: 2024-05-19 14:07:13.962707

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '83401bb3e69d'
down_revision = '7f4c1ea6c8c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.UUID(),
               type_=sa.String(length=36),
               existing_nullable=False)
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=256),
               existing_nullable=True)
        batch_op.alter_column('inventory_items',
               existing_type=postgresql.ARRAY(sa.UUID()),
               type_=postgresql.ARRAY(sa.String(length=36)),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('inventory_items',
               existing_type=postgresql.ARRAY(sa.String(length=36)),
               type_=postgresql.ARRAY(sa.UUID()),
               existing_nullable=True)
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=128),
               existing_nullable=True)
        batch_op.alter_column('user_id',
               existing_type=sa.String(length=36),
               type_=sa.UUID(),
               existing_nullable=False)

    # ### end Alembic commands ###
