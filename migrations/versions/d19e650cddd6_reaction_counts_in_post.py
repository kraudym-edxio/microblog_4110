"""reaction_counts_in_post

Revision ID: d19e650cddd6
Revises: bac3b2625d32
Create Date: 2023-03-10 14:32:54.670956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd19e650cddd6'
down_revision = 'bac3b2625d32'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('reaction_like', sa.Integer()))
    op.add_column('post', sa.Column('reaction_dislike', sa.Integer()))
    op.add_column('post', sa.Column('reaction_heart', sa.Integer()))
    op.add_column('post', sa.Column('reaction_laugh', sa.Integer()))
    op.add_column('post', sa.Column('reaction_angry', sa.Integer()))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'reaction_like')
    op.drop_column('post', 'reaction_dislike')
    op.drop_column('post', 'reaction_heart')
    op.drop_column('post', 'reaction_laugh')
    op.drop_column('post', 'reaction_angry')
    # ### end Alembic commands ###
