"""empty message

Revision ID: 6e68227079ae
Revises: b58d3c016cad
Create Date: 2024-05-19 16:02:44.180298

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6e68227079ae'
down_revision = 'b58d3c016cad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    op.drop_table('transaction')
    op.drop_table('user')
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('product_id', sa.UUID(), nullable=False))
        batch_op.add_column(sa.Column('condition', sa.String(length=80), nullable=False))
        batch_op.add_column(sa.Column('images', postgresql.ARRAY(sa.String()), nullable=True))
        batch_op.drop_column('id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
        batch_op.drop_column('images')
        batch_op.drop_column('condition')
        batch_op.drop_column('product_id')

    op.create_table('user',
    sa.Column('user_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('password_hash', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('username', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('profile', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('inventory_items', postgresql.ARRAY(sa.UUID()), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('user_id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key'),
    sa.UniqueConstraint('username', name='user_username_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('transaction',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('amount', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('type', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='transaction_pkey')
    )
    op.create_table('order',
    sa.Column('order_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('product_details', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('price', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('status', postgresql.ENUM('open', 'matched', 'closed', name='order_statuses'), autoincrement=False, nullable=False),
    sa.Column('order_type', postgresql.ENUM('buy', 'sell', name='order_types'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], name='order_user_id_fkey'),
    sa.PrimaryKeyConstraint('order_id', name='order_pkey')
    )
    # ### end Alembic commands ###
