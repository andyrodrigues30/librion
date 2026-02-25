from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base

from db.models.associations import book_authors, book_genres


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    series_name = Column(String(255))
    series_number = Column(Integer)
    cover_img_url = Column(String(255))
    summary = Column(Text)
    pages = Column(Integer)
    published_date = Column(Date)
    purchased_date = Column(Date)

    format_id = Column(Integer, ForeignKey("formats.id", ondelete="SET NULL"))

    # relationships
    authors = relationship("Author", secondary=book_authors, back_populates="books")
    genres = relationship("Genre", secondary=book_genres, back_populates="books")
    format = relationship("Format", back_populates="books")