"""empty message

Revision ID: 8ae4ed878242
Revises: 71f44d0ece1e
Create Date: 2020-11-28 16:01:42.068515

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ae4ed878242'
down_revision = '71f44d0ece1e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_description', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'seeking_description')
    # ### end Alembic commands ###
