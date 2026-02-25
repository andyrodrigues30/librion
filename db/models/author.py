from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base

from models.book import book_authors


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)

    # relationships
    books = relationship("Book", secondary=book_authors,
                         back_populates="authors")
