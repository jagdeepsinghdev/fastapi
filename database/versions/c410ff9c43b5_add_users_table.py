"""add users table

Revision ID: c410ff9c43b5
Revises: 299c8676c932
Create Date: 2022-01-18 00:53:11.761764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c410ff9c43b5"
down_revision = "299c8676c932"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    pass


def downgrade():
    op.drop_table("users")
    pass
