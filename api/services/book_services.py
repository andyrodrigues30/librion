from fastapi import HTTPException
from sqlalchemy.orm import joinedload

from api.schemas import book_schemas
from db.models import book_models


def get_books(db):
    """Get all book entries."""
    return db.query(book_models.Book).options(joinedload(book_models.Book.authors)).all()


def get_book_by_id(id: int, db):
    """Get book by id."""
    book = db.query(book_models.Book).join(book_models.Book.authors).filter(book_models.Book.id == id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
    

def add_book(book: book_schemas.BookCreate, db):
    """Create a new book entry."""
    new_book = book_models.Book(title=book.title, author=book.author, summary=book.summary, pages=book.pages, published_date=book.published_date, purchased_date=book.purchased_date)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)# reload from DB to get generated ID
    return new_book


def edit_book(id: int, updated_book: book_schemas.BookUpdate, db):
    book = db.query(book_models.Book).filter(book_models.Book.id == id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # only update fields that are provided
    if updated_book.title is not None:
        book.title = updated_book.title
    if updated_book.author is not None:
        book.author = updated_book.author
    if updated_book.summary is not None:
        book.summary = updated_book.summary
    if updated_book.pages is not None:
        book.pages = updated_book.pages
    if updated_book.published_date is not None:
        book.published_date = updated_book.published_date
    if updated_book.purchased_date is not None:
        book.purchased_date = updated_book.purchased_date

    db.commit()
    db.refresh(book)
    return book


def delete_book(id: int, db):
    book = db.query(book_models.Book).filter(book_models.Book.id == id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db.delete(book)
    db.commit()
    return { "detail": f"Book with id {id} successfully deleted" }