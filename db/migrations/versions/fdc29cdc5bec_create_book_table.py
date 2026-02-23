"""create book table

Revision ID: fdc29cdc5bec
Revises: 
Create Date: 2026-02-23 14:24:07.264020

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column, select


# revision identifiers, used by Alembic.
revision: str = 'fdc29cdc5bec'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    
    # create book table
    op.create_table('books',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('author', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_books_id'), 'books', ['id'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    
    # drop books table
    op.drop_index(op.f('ix_books_id'), table_name='books')
    op.drop_table('books')
