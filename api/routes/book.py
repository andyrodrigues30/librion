from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from api.schemas.book import BookBase, BookCreate, BookRead
from api.schemas.response import DetailsResponse
from api.services.book import get_all_books, get_book_by_id, add_book, search_books, edit_book, remove_book


router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=list[BookBase])
def books(db: Session = Depends(get_db)):
    return get_all_books(db)


@router.get("/search/", response_model=List[BookRead])
def search(
    q: str = Query(..., description="Search query string for title, author, genre, or format"),
    db: Session = Depends(get_db),
):
    return search_books(db, q)


@router.get("/{id}", response_model=BookBase)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return get_book_by_id(db, id)


@router.post("/", response_model=BookBase)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return add_book(db, book)


@router.put("/{id}", response_model=BookBase)
def edit_book(id: int, new_book: BookBase, db: Session = Depends(get_db)):
    return edit_book(db, id, new_book)


@router.delete("/{id}", status_code=200, response_model=DetailsResponse)
def delete_book(id: int, db: Session = Depends(get_db)):
    return remove_book(db, id)
