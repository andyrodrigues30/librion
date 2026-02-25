from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from api.schemas.format import FormatCreate, FormatRead
from api.services.format import get_all_formats, add_format, edit_format, remove_format

router = APIRouter(prefix="/format", tags=["Format"])


@router.get("/", response_model=list[FormatRead])
def get_format(db: Session = Depends(get_db)):
    return get_all_formats(db)


@router.post("/", response_model=FormatRead)
def add_format(genre: FormatCreate, db: Session = Depends(get_db)):
    return add_format(db, genre)


@router.put("/{genre_id}", response_model=FormatRead)
def update_format_endpoint(genre_id: int, genre: FormatCreate, db: Session = Depends(get_db)):
    db_genre = edit_format(db, genre_id, genre)
    if not db_genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    return db_genre


@router.delete("/{genre_id}", response_model=FormatRead)
def delete_format_endpoint(genre_id: int, db: Session = Depends(get_db)):
    db_genre = remove_format(db, genre_id)
    if not db_genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    return db_genre
