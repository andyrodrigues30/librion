from sqlalchemy.orm import Session

from db.models import Genre
from api.schemas.genre import GenreCreate


def get_all_genres(db: Session):
    return db.query(Genre).all()


def get_genre_by_id(db: Session, id: int):
    return db.query(Genre).filter(Genre.id == id).first()


def add_genre(db: Session, genre: GenreCreate):
    db_genre = Genre(name=genre.name)
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre


def edit_genre(db: Session, id: int, genre_data: GenreCreate):
    db_genre = get_genre_by_id(db, id)
    if not db_genre:
        return None
    db_genre.name = genre_data.name
    db.commit()
    db.refresh(db_genre)
    return db_genre


def remove_genre(db: Session, id: int):
    db_genre = get_genre_by_id(db, id)
    if not db_genre:
        return None
    db.delete(db_genre)
    db.commit()
    return db_genre
