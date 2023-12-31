"""empty message

Revision ID: dea737262fd3
Revises: cd17189d7457
Create Date: 2023-07-31 08:11:25.305993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dea737262fd3'
down_revision = 'cd17189d7457'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('songs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('artwork', sa.String(length=64), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('songs', schema=None) as batch_op:
        batch_op.drop_column('artwork')

    # ### end Alembic commands ###
