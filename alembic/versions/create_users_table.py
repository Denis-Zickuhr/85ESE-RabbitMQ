"""Create users table

author : Denis Zickuhr
Create Date: 2022-01-01 00:00:00

"""

from alembic import op
import sqlalchemy as sa


revision = 'create_users_table'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('gender', sa.String(10)),
        sa.Column('title', sa.String(10)),
        sa.Column('first_name', sa.String(50)),
        sa.Column('last_name', sa.String(50)),
        sa.Column('street_number', sa.Integer),
        sa.Column('street_name', sa.String(100)),
        sa.Column('city', sa.String(100)),
        sa.Column('state', sa.String(100)),
        sa.Column('country', sa.String(100)),
        sa.Column('postcode', sa.String(20)),
        sa.Column('latitude', sa.String(20)),
        sa.Column('longitude', sa.String(20)),
        sa.Column('timezone_offset', sa.String(20)),
        sa.Column('timezone_description', sa.String(100)),
        sa.Column('email', sa.String(100)),
        sa.Column('username', sa.String(50)),
        sa.Column('password', sa.String(100)),
        sa.Column('dob_date', sa.DateTime),
        sa.Column('dob_age', sa.Integer),
        sa.Column('registered_date', sa.DateTime),
        sa.Column('registered_age', sa.Integer),
        sa.Column('phone', sa.String(20)),
        sa.Column('cell', sa.String(20)),
        sa.Column('id_name', sa.String(50)),
        sa.Column('id_value', sa.String(100)),
        sa.Column('picture_large', sa.String(200)),
        sa.Column('picture_medium', sa.String(200)),
        sa.Column('picture_thumbnail', sa.String(200)),
        sa.Column('nationality', sa.String(10))
    )


def downgrade():
    op.drop_table('users')
