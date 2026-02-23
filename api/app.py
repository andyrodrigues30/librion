from fastapi import FastAPI
from api.routes import book_routes, scraper_routes

app = FastAPI(title="Books API")

app.include_router(book_routes.router)
app.include_router(scraper_routes.router)