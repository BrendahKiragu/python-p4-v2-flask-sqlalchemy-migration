"""renames department

Revision ID: 29477a71c301
Revises: 9f72f58aad8a
Create Date: 2024-10-01 13:26:21.878285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29477a71c301'
down_revision = '9f72f58aad8a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
