from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, publised_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = publised_date

class BookRequest(BaseModel):
    id: int = Field(description = "ID is not required on create", default = None)
    title: str = Field(min_length = 3)
    author:str = Field(min_length = 1)
    description: str = Field(min_length = 1, max_length = 30)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(min_length = 4)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "author name",
                "description": "A new description for the book",
                "rating": 5,
                "published_date": "2002"
            }
        }
    }

BOOKS = [
    Book(1, 'Computer Science Pro', 'kcabhish', 'Awesome Book', 5, 2001),
    Book(2, 'Fast API', 'John', 'Learn Fast API', 5, 2002),
    Book(3, 'Learn pydantic', 'John', 'Books for type checkings', 4, 2003),
    Book(4, 'Witcher', 'Swe', 'Awesome game and a book', 5, 2002),
    Book(5, 'LOTR', 'Tolken', 'Story of hobbit trying to destroy ring of power', 3, 1972),
]

@app.get("/books")
async def get_all_books():
    return BOOKS

@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(set_book_id(new_book))

def set_book_id(book: Book):
    if (len(BOOKS) > 0):
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1
    return book

@app.get("/books/{book_id}")
async def read_book_by_id(book_id: int):
    """
    Fetch book by ID
    """
    for book in BOOKS:
        if (book_id == book.id):
           return book
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/books/")
async def read_book_by_rating(rating: int = Query(gt = 0, lt=6)):
    """
    Fetch books by ratings
    """
    books_to_return = []
    for book in BOOKS:
        if (rating == book.rating):
            books_to_return.append(book)
    return books_to_return

@app.get("/books/publish/{publish_date}")
async def read_books_by_publish_date(publish_date: int):
    list_of_books = []
    for book in BOOKS:
        if (book.published_date == publish_date):
            list_of_books.append(book)
        
    return list_of_books


@app.delete("/books/{book_id}")
async def delete_book(book_id:int = Path(gt = 0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break