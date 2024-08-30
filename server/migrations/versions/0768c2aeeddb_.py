"""empty message

Revision ID: 0768c2aeeddb
Revises: 82627c7da64d
Create Date: 2024-08-29 20:08:32.405650

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0768c2aeeddb'
down_revision = '82627c7da64d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.String(length=200), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.drop_column('image')

    # ### end Alembic commands ###
