from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from api.schemas.genre import GenreCreate, GenreRead
from api.services.genre import get_all_genres, get_genre_by_id, add_genre, edit_genre, remove_genre

router = APIRouter(prefix="/genres", tags=["Genres"])


@router.get("/", response_model=list[GenreRead])
def get_genres(db: Session = Depends(get_db)):
    return get_all_genres(db)


@router.get("/{id}", response_model=GenreRead)
def read_genre(id: int, db: Session = Depends(get_db)):
    db_genre = get_genre_by_id(db, id)
    if not db_genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    return db_genre


@router.post("/", response_model=GenreRead)
def add_genre(genre: GenreCreate, db: Session = Depends(get_db)):
    return add_genre(db, genre)


@router.put("/{id}", response_model=GenreRead)
def update_genre_endpoint(id: int, genre: GenreCreate, db: Session = Depends(get_db)):
    db_genre = edit_genre(db, id, genre)
    if not db_genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    return db_genre


@router.delete("/{id}", response_model=GenreRead)
def delete_genre_endpoint(id: int, db: Session = Depends(get_db)):
    db_genre = remove_genre(db, id)
    if not db_genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    return db_genre
