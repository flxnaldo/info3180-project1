"""empty message

Revision ID: f2a689164444
Revises: 
Create Date: 2021-03-22 19:02:04.981903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2a689164444'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('house_properties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('num_bedrooms', sa.String(), nullable=True),
    sa.Column('num_bathrooms', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('price', sa.String(), nullable=True),
    sa.Column('property_type', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('photo', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('house_properties')
    # ### end Alembic commands ###