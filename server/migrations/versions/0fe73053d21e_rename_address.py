"""rename address

Revision ID: 0fe73053d21e
Revises: fa0b2a381c49
Create Date: 2025-03-25 15:27:14.997774

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fe73053d21e'
down_revision = 'fa0b2a381c49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',  new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
     op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###
