"""add foreignkey to posts table

Revision ID: b96a149b0ef8
Revises: c410ff9c43b5
Create Date: 2022-01-18 00:58:03.246787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b96a149b0ef8"
down_revision = "c410ff9c43b5"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "post_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("post", "owner_id")
    pass
