from fastapi import APIRouter

from api.services.scraper import get_gr_data


router = APIRouter(prefix="/scraper", tags=["Scraper"])


@router.get("/")
def gr_book_data(URL: str):
    return get_gr_data(URL)
