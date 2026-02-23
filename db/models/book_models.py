from sqlalchemy import Column, Integer, String, TEXT, Date
from sqlalchemy.orm import relationship
from db.database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    summary = Column(TEXT)
    pages = Column(Integer)
    published_date = Column(Date)
    purchased_date = Column(Date)


    authors = relationship(
        "Author",
        secondary="book_authors",
        back_populates="books"
    )


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)

    books = relationship(
        "Book",
        secondary="book_authors",
        back_populates="authors"
    )