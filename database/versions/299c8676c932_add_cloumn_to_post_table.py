"""add cloumn to post table

Revision ID: 299c8676c932
Revises: f9c253c6c1b1
Create Date: 2022-01-17 23:45:42.808246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "299c8676c932"
down_revision = "f9c253c6c1b1"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("content", sa.String(), nullable=False),
    )
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
