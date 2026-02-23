from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Librion API")

books = [
  {"id": 1, "title": "The Giver", "author": "Lois Lowry"},
  {"id": 2, "title": "Fahrenheit 451", "author": "Ray Bradbury"},
  {"id": 3, "title": "The Hunger Games", "author": "Suzanne Collins"},
  {"id": 4, "title": "Animal Farm", "author": "George Orwell"}
]


@app.get("/")
def hello():
  return {"hello": "world"}


class Book(BaseModel):
  id: int
  title: str
  author: str

class BookCreate(BaseModel):
  title: str
  author: str

# get list of all books
@app.get("/books")
def get_books():
  return books


# get a book by its id
@app.get("/books", response_model=Book)
def get_book_by_id(id: int):
  # loop through all books
  for book in books:
    if book["id"] == id:
      # if the id matches the id in the request - return the data
      return book
    else:
      # if the id DOES NOT match the request - return error message
      raise HTTPException(status_code=404, detail="Book not found")
      

  
# edit book
@app.put("/books/{:id}", response_model=Book)
def edit_book(id:int, updated_book: BookCreate):
  for book in books:
        if book["id"] == id:
            # Update existing fields
            book["title"] = updated_book.title
            book["author"] = updated_book.author
            return book
  raise HTTPException(status_code=404, detail="Book not found")


# delete book
  
@app.delete("/books/{:id}", status_code=204)
def edit_book(id:int):
  for index, book in enumerate(books):
        if book["id"] == id:
            books.pop(index)
            return  # 204 means "No Content", so no response body
  raise HTTPException(status_code=404, detail="Book not found")