"""update book schema and add genres/formats

Revision ID: c45e725e7ce1
Revises: e6e5e3c250fa
Create Date: 2026-02-25 12:32:51.341072

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c45e725e7ce1'
down_revision: Union[str, Sequence[str], None] = 'e6e5e3c250fa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # create formats table first
    op.create_table(
        "formats",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("type", sa.String(length=255), nullable=False, unique=True)
    )

    # create genres table
    op.create_table(
        "genres",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=255), nullable=False, unique=True)
    )

    # create association table for book_genres
    op.create_table(
        "book_genres",
        sa.Column("book_id", sa.Integer(), sa.ForeignKey("books.id", ondelete="CASCADE"), primary_key=True),
        sa.Column("genre_id", sa.Integer(), sa.ForeignKey("genres.id", ondelete="CASCADE"), primary_key=True)
    )

    # add new columns to books table
    op.add_column('books', sa.Column('series_name', sa.String(length=255), nullable=True))
    op.add_column('books', sa.Column('series_number', sa.Integer(), nullable=True))
    op.add_column('books', sa.Column('cover_img_url', sa.String(length=255), nullable=True))
    op.add_column('books', sa.Column('format_id', sa.Integer(), nullable=True))

    # add foreign key constraint to format
    op.create_foreign_key(
        "fk_books_format",
        "books", "formats",
        ["format_id"], ["id"],
        ondelete="SET NULL"
    )


def downgrade() -> None:
    # drop foreign key first
    op.drop_constraint("fk_books_format", "books", type_="foreignkey")

    # drop added columns from books table
    op.drop_column("books", "format_id")
    op.drop_column("books", "cover_img_url")
    op.drop_column("books", "series_number")
    op.drop_column("books", "series_name")

    # drop book_genres association table
    op.drop_table("book_genres")

    # drop genres and formats tables
    op.drop_table("genres")
    op.drop_table("formats")