from pydantic import BaseModel
from typing import List, Optional
from datetime import date

from api.schemas.author import AuthorRead
from api.schemas.format import FormatRead
from api.schemas.genre import GenreRead


class BookBase(BaseModel):
    title: str
    series_name: Optional[str]
    series_number: Optional[int]
    cover_img_url: Optional[str]
    summary: Optional[str]
    pages: Optional[int]
    published_date: Optional[date]

    format_id: Optional[int] = None
    author_ids: Optional[List[int]] = []
    genre_ids: Optional[List[int]] = []

    format_type: Optional[str] = None
    author_names: Optional[List[str]] = []
    genre_names: Optional[List[str]] = []


class BookCreate(BookBase):
    pass


class BookRead(BookBase):
    id: int
    authors: List[AuthorRead] = []
    genres: List[GenreRead] = []
    format: Optional[FormatRead]

    class Config:
        from_attributes = True