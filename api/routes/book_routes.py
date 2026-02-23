from fastapi import APIRouter, Depends
from api.schemas import book_schemas, response_schema
from api.services import book_services

from sqlalchemy.orm import Session
from db.database import get_db


router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=list[book_schemas.BookBase])
def books(db: Session = Depends(get_db)):
    return book_services.get_books(db)


@router.get("/{id}", response_model=book_schemas.BookBase)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return book_services.get_book_by_id(id, db)


@router.post("/", response_model=book_schemas.BookBase)
def add_book(book: book_schemas.BookCreate, db: Session = Depends(get_db)):
    return book_services.add_book(book, db)


@router.put("/{id}", response_model=book_schemas.BookBase)
def edit_book(id: int, new_book: book_schemas.BookUpdate, db: Session = Depends(get_db)):
    return book_services.edit_book(id, new_book, db)


@router.delete("/{id}", status_code=200, response_model=response_schema.DetailsResponse)
def delete_book(id: int, db: Session = Depends(get_db)):
    return book_services.delete_book(id, db)