from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from api.schemas.author import AuthorCreate, AuthorRead
from api.services.author import get_all_authors, get_author_by_id, add_author, edit_author, remove_author

router = APIRouter(prefix="/authors", tags=["Authors"])


@router.get("/", response_model=List[AuthorRead])
def get_authors(db: Session = Depends(get_db)):
    return get_all_authors(db)


@router.get("/{id}", response_model=AuthorRead)
def get_author(id: int, db: Session = Depends(get_db)):
    db_author = get_author_by_id(db, id)
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author


@router.post("/", response_model=AuthorRead)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    return add_author(db, author)


@router.put("/{id}", response_model=AuthorRead)
def update_author(id: int, author: AuthorCreate, db: Session = Depends(get_db)):
    db_author = edit_author(db, id, author)
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author


@router.delete("/{id}", response_model=AuthorRead)
def delete_author_endpoint(id: int, db: Session = Depends(get_db)):
    db_author = remove_author(db, id)
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author
