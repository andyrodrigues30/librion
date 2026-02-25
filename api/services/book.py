from sqlalchemy import or_
from sqlalchemy.orm import Session, joinedload

from db.models import Book, Author, Genre, Format
from api.schemas.book import BookCreate


def get_all_books(db: Session):
    return (
        db.query(Book)
        .options(
            joinedload(Book.authors),
            joinedload(Book.genres),
            joinedload(Book.format),
        )
        .all()
    )


def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def search_books(db: Session, q: str):
    search = f"%{q}%"

    query = (
        db.query(Book)
        .options(
            joinedload(Book),
            joinedload(Book.genres),
            joinedload(Book.format),
        )
        .outerjoin(Book.authors)
        .outerjoin(Book.genres)
        .outerjoin(Book.format)
        .filter(
            or_(
                Book.title.ilike(search),
                Book.series_name.ilike(search),
                Author.name.ilike(search),
                Genre.name.ilike(search),
                Format.type.ilike(search),
            )
        )
        .distinct()
    )

    return query.all()


def add_book(db: Session, book: BookCreate):
    db_book = Book(
        title=book.title,
        series_name=book.series_name,
        series_number=book.series_number,
        cover_img_url=book.cover_img_url,
        summary=book.summary,
        pages=book.pages,
        published_date=book.published_date,
        format_id=book.format_id  # set if provided
    )

    # format
    if book.format_type:
        fmt = db.query(Format).filter_by(type=book.format_type).first()
        if not fmt:
            fmt = Format(type=book.format_type)
            db.add(fmt)
            db.commit()
            db.refresh(fmt)
        db_book.format = fmt

    # authors
    authors = []
    if book.author_ids:
        authors += db.query(Author).filter(Author.id.in_(book.author_ids)).all()
    if book.author_names:
        for name in book.author_names:
            author = db.query(Author).filter_by(name=name).first()
            if not author:
                author = Author(name=name)
                db.add(author)
                db.commit()
                db.refresh(author)
            authors.append(author)
    db_book.authors = authors

    # genres
    genres = []
    if book.genre_ids:
        genres += db.query(Genre).filter(Genre.id.in_(book.genre_ids)).all()
    if book.genre_names:
        for name in book.genre_names:
            genre = db.query(Genre).filter_by(name=name).first()
            if not genre:
                genre = Genre(name=name)
                db.add(genre)
                db.commit()
                db.refresh(genre)
            genres.append(genre)
    db_book.genres = genres

    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def edit_book(db: Session, book_id: int, book: BookCreate):
    db_book = db.query(Book).filter_by(id=book_id).first()
    if not db_book:
        return None

    # update basic fields
    for field in ["title", "series_name", "series_number", "cover_img_url",
                  "summary", "pages", "published_date", "format_id"]:
        if getattr(book, field) is not None:
            setattr(db_book, field, getattr(book, field))

    # format
    if book.format_type:
        fmt = db.query(Format).filter_by(type=book.format_type).first()
        if not fmt:
            fmt = Format(type=book.format_type)
            db.add(fmt)
            db.commit()
            db.refresh(fmt)
        db_book.format = fmt

    # authors
    authors = []
    if book.author_ids:
        authors += db.query(Author).filter(Author.id.in_(book.author_ids)).all()
    if book.author_names:
        for name in book.author_names:
            author = db.query(Author).filter_by(name=name).first()
            if not author:
                author = Author(name=name)
                db.add(author)
                db.commit()
                db.refresh(author)
            authors.append(author)
    if authors:
        db_book.authors = authors

    # genres
    genres = []
    if book.genre_ids:
        genres += db.query(Genre).filter(Genre.id.in_(book.genre_ids)).all()
    if book.genre_names:
        for name in book.genre_names:
            genre = db.query(Genre).filter_by(name=name).first()
            if not genre:
                genre = Genre(name=name)
                db.add(genre)
                db.commit()
                db.refresh(genre)
            genres.append(genre)
    if genres:
        db_book.genres = genres

    db.commit()
    db.refresh(db_book)
    return db_book

def remove_book(db: Session, id: int):
    db_book = get_book_by_id(db, id)
    if not db_book:
        return None

    db.delete(db_book)
    db.commit()
    return db_book
