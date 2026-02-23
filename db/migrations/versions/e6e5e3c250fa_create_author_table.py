"""create author table

Revision ID: e6e5e3c250fa
Revises: e7e3626a3588
Create Date: 2026-02-23 14:52:19.244454

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column, select


# revision identifiers, used by Alembic.
revision: str = 'e6e5e3c250fa'
down_revision: Union[str, Sequence[str], None] = 'e7e3626a3588'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
   
   # create authors table
    op.create_table(
        "authors",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(length=255), nullable=False, unique=True)
    )
    
    # create association table
    op.create_table(
        "book_authors",
        sa.Column("book_id", sa.Integer(), nullable=False),
        sa.Column("author_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["book_id"], ["books.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["author_id"], ["authors.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("book_id", "author_id")
    )

    # prepare table references
    books = table(
        "books",
        column("id", sa.Integer),
        column("author", sa.String),
    )

    authors = table(
        "authors",
        column("id", sa.Integer),
        column("name", sa.String),
    )

    book_authors = table(
        "book_authors",
        column("book_id", sa.Integer),
        column("author_id", sa.Integer),
    )

    conn = op.get_bind()

    # fetch all existing books with authors
    results = conn.execute(
        select(books.c.id, books.c.author).where(books.c.author.isnot(None))
    ).fetchall()

    author_cache = {}

    for book_id, author_name in results:
        author_name = author_name.strip()

        if not author_name:
            continue

        # insert author if not already created
        if author_name not in author_cache:
            res = conn.execute(
                authors.insert()
                .values(name=author_name)
                .returning(authors.c.id)
            )
            author_id = res.scalar()
            author_cache[author_name] = author_id
        else:
            author_id = author_cache[author_name]

        # link book to author
        conn.execute(
            book_authors.insert().values(
                book_id=book_id,
                author_id=author_id,
            )
        )

    # drop old author column
    op.drop_column("books", "author")


def downgrade() -> None:
    """Downgrade schema."""
    
    # add author column
    op.add_column(
        "books",
        sa.Column("author", sa.String(length=255), nullable=True),
    )

    conn = op.get_bind()

    # add author names back to books.author
    conn.execute(
        sa.text(
            """
            UPDATE books
            SET author = sub.name
            FROM (
                SELECT ba.book_id, a.name
                FROM book_authors ba
                JOIN authors a ON a.id = ba.author_id
            ) sub
            WHERE books.id = sub.book_id
            """
        )
    )

    # drop association & authors tables
    op.drop_table("book_authors")
    op.drop_table("authors")
