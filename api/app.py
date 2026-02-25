from fastapi import FastAPI

from api.routes import book, author, genre, format, scraper

app = FastAPI(title="Books API")

app.include_router(book.router)
app.include_router(author.router)
app.include_router(genre.router)
app.include_router(format.router)
app.include_router(scraper.router)