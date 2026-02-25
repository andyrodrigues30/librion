"""add uniqueness to author genre format

Revision ID: b818c448dba4
Revises: c45e725e7ce1
Create Date: 2026-02-25 14:30:58.298134

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b818c448dba4'
down_revision: Union[str, Sequence[str], None] = 'c45e725e7ce1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_unique_constraint(
        "uq_authors_name",
        "authors",
        ["name"]
    )

    op.create_unique_constraint(
        "uq_genres_name",
        "genres",
        ["name"]
    )

    op.create_unique_constraint(
        "uq_formats_type",
        "formats",
        ["type"]
    )


def downgrade():
    op.drop_constraint("uq_formats_type", "formats", type_="unique")
    op.drop_constraint("uq_genres_name", "genres", type_="unique")
    op.drop_constraint("uq_authors_name", "authors", type_="unique")
