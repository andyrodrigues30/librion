from sqlalchemy.orm import Session

from db.models import Author
from api.schemas.author import AuthorCreate


def get_all_authors(db: Session):
    return db.query(Author).all()


def get_author_by_id(db: Session, id: int):
    return db.query(Author).filter(Author.id == id).first()


def add_author(db: Session, author: AuthorCreate):
    db_author = Author(name=author.name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def edit_author(db: Session, id: int, author_data: AuthorCreate):
    db_author = get_author_by_id(db, id)
    if not db_author:
        return None
    db_author.name = author_data.name
    db.commit()
    db.refresh(db_author)
    return db_author


def remove_author(db: Session, id: int):
    db_author = get_author_by_id(db, id)
    if not db_author:
        return None
    db.delete(db_author)
    db.commit()
    return db_author
