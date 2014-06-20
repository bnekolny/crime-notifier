"""create crime table.

Revision ID: 10b0c982a45a
Revises: None
Create Date: 2014-03-23 23:54:23.006181

"""

# revision identifiers, used by Alembic.
revision = '10b0c982a45a'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('policedepartment_registry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('city', sa.String(length=10), nullable=True),
    sa.Column('state', sa.String(length=2), nullable=True),
    sa.Column('data_source_url', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('crimes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pd_id', sa.Integer(), nullable=True),
    sa.Column('pd_incident', sa.Integer(), nullable=True),
    sa.Column('pd_offense', sa.Integer(), nullable=True),
    sa.Column('offense_code_id', sa.Integer(), nullable=True),
    sa.Column('offense_code_ext_id', sa.Integer(), nullable=True),
    sa.Column('offense_type', sa.String(length=20), nullable=True),
    sa.Column('offense_category', sa.String(length=20), nullable=True),
    sa.Column('first_occurrence', sa.DateTime(), nullable=True),
    sa.Column('last_occurrence', sa.DateTime(), nullable=True),
    sa.Column('reported_date', sa.DateTime(), nullable=True),
    sa.Column('address', sa.String(length=20), nullable=True),
    sa.Column('geo_x', sa.Float(), nullable=True),
    sa.Column('geo_y', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('pd_district', sa.Integer(), nullable=True),
    sa.Column('pd_precinct', sa.Integer(), nullable=True),
    sa.Column('neighborhood', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['pd_id'], ['policedepartment_registry.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('crimes')
    op.drop_table('policedepartment_registry')
    ### end Alembic commands ###