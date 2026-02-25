from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.database import Base
from db.models.associations import book_authors


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True, index=True)

    # relationship
    books = relationship(
        "Book",
        secondary=book_authors,
        back_populates="authors"
    )