"""empty message

Revision ID: 73786f965c8b
Revises: 
Create Date: 2022-05-11 22:45:45.426950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73786f965c8b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
