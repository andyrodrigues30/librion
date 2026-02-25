from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.database import Base
from db.models.associations import book_genres


class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True, index=True)

    # relationship
    books = relationship(
        "Book",
        secondary=book_genres,
        back_populates="genres"
    )