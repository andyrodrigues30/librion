"""add columns to book table

Revision ID: e7e3626a3588
Revises: fdc29cdc5bec
Create Date: 2026-02-23 14:49:33.169219

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e7e3626a3588'
down_revision: Union[str, Sequence[str], None] = 'fdc29cdc5bec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    # add new columns
    op.add_column('books', sa.Column('summary', sa.TEXT(), nullable=True))
    op.add_column('books', sa.Column('pages', sa.Integer(), nullable=True))
    op.add_column('books', sa.Column('published_date', sa.Date(), nullable=True))
    op.add_column('books', sa.Column('purchased_date', sa.Date(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""

    # drop new columns
    op.drop_column('books', 'purchased_date')
    op.drop_column('books', 'published_date')
    op.drop_column('books', 'pages')
    op.drop_column('books', 'summary')
