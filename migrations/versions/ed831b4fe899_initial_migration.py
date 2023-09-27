"""Initial migration

Revision ID: ed831b4fe899
Revises: 
Create Date: 2023-09-27 00:00:00

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic
revision = 'ed831b4fe899'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'restaurants',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('address', sa.String(length=100), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'pizza',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('ingredients', sa.String(length=200), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'restaurant_pizza',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('price', sa.Float(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('restaurant_id', sa.Integer(), nullable=False),
        sa.Column('pizza_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
        sa.ForeignKeyConstraint(['pizza_id'], ['pizza.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('restaurant_pizza')
    op.drop_table('pizza')
    op.drop_table('restaurants')
