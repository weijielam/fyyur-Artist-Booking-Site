"""empty message

Revision ID: 151253ac6b18
Revises: 55b217dee4fe
Create Date: 2020-10-03 18:54:04.195836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '151253ac6b18'
down_revision = '55b217dee4fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.add_column('Venue', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    
    op.execute("UPDATE \"Artist\" SET seeking_venue = false")
    op.alter_column('Artist', 'seeking_venue', nullable=False)
    
    op.execute("UPDATE \"Venue\" SET seeking_talent = false")
    op.alter_column('Venue', 'seeking_talent', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'seeking_talent')
    op.drop_column('Artist', 'seeking_venue')
    # ### end Alembic commands ###
