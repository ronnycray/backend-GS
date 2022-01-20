"""Create models for devices

Revision ID: 6f2642823372
Revises: eb743fc45970
Create Date: 2021-09-30 17:08:44.678914

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f2642823372'
down_revision = 'eb743fc45970'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('devices',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('device_id', sa.VARCHAR(length=255), nullable=False),
    sa.Column('last_authentication', sa.TIMESTAMP(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_devices_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_devices'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('devices')
    # ### end Alembic commands ###
