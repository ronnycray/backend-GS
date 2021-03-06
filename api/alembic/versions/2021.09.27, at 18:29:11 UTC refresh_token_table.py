"""Refresh token table

Revision ID: 1714c22ac0b5
Revises: d7296b2bec91
Create Date: 2021-09-27 18:29:11.952223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1714c22ac0b5'
down_revision = 'd7296b2bec91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('refresh_tokens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('refresh_token', sa.VARCHAR(length=255), nullable=False),
    sa.Column('expires_at', sa.TIMESTAMP(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_refresh_tokens_user_id_user')),
    sa.PrimaryKeyConstraint('id', 'user_id', name=op.f('pk_refresh_tokens')),
    sa.UniqueConstraint('refresh_token', name=op.f('uq_refresh_tokens_refresh_token'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('refresh_tokens')
    # ### end Alembic commands ###
