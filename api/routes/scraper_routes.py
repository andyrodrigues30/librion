from fastapi import APIRouter
from api.services import scraper_services


router = APIRouter(prefix="/scraper", tags=["Scraper"])


@router.get("/")
def gr_book_data(URL: str):
    return scraper_services.get_book_data(URL)




