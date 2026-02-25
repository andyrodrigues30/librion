from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base

from models.book import book_genres


class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)

    # relationships
    books = relationship("Book", secondary=book_genres,
                         back_populates="genres")
