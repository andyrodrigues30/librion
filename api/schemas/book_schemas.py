from pydantic import BaseModel
from datetime import date
from typing import List
from api.schemas.author_schemas import AuthorBase, AuthorCreate


class BookBase(BaseModel):
    id: int
    title: str
    authors: List[AuthorBase]
    summary: str | None = None
    pages: int | None = None
    published_date: date | None = None
    purchased_date: date | None = None


class BookCreate(BaseModel):
    title: str
    authors: List[AuthorCreate]
    summary: str
    pages: int
    published_date: date | None = None
    purchased_date: date | None = None


class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    summary: str | None = None
    pages: int | None = None
    published_date: date | None = None
    purchased_date: date | None = None
