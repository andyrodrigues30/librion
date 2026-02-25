from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, Table
from sqlalchemy.orm import relationship

from database import Base

# association tables
book_authors = Table(
    "book_authors",
    Base.metadata,
    Column("book_id", Integer, ForeignKey(
        "books.id", ondelete="CASCADE"), primary_key=True),
    Column("author_id", Integer, ForeignKey(
        "authors.id", ondelete="CASCADE"), primary_key=True),
)

book_genres = Table(
    "book_genres",
    Base.metadata,
    Column("book_id", Integer, ForeignKey(
        "books.id", ondelete="CASCADE"), primary_key=True),
    Column("genre_id", Integer, ForeignKey(
        "genres.id", ondelete="CASCADE"), primary_key=True),
)


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    series_name = Column(String(255), nullable=True)
    series_number = Column(Integer, nullable=True)
    cover_img_url = Column(String(255), nullable=True)
    summary = Column(Text, nullable=True)
    pages = Column(Integer, nullable=True)
    published_date = Column(Date, nullable=True)
    purchased_date = Column(Date, nullable=True)

    # relationships
    authors = relationship(
        "Author", secondary=book_authors, back_populates="books")
    genres = relationship("Genre", secondary=book_genres,
                          back_populates="books")
    format_id = Column(Integer, ForeignKey(
        "formats.id", ondelete="SET NULL"), nullable=True)
    format = relationship("Format", back_populates="books")
