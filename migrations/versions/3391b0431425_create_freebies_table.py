"""Create freebies table

Revision ID: 3391b0431425
Revises: 
Create Date: 2025-05-25 11:06:30.233752

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3391b0431425'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'freebies',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('item_name', sa.String()),
        sa.Column('value', sa.Integer()),
        sa.Column('dev_id', sa.Integer(), sa.ForeignKey('devs.id')),
        sa.Column('company_id', sa.Integer(), sa.ForeignKey('companies.id')),
    )

def downgrade() -> None:
    op.drop_table('freebies')

