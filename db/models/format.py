from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.database import Base


class Format(Base):
    __tablename__ = "formats"

    id = Column(Integer, primary_key=True)
    type = Column(String(255), nullable=False, unique=True, index=True)

    # relationship
    books = relationship("Book", back_populates="format")
