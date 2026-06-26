from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [{"title": "Witcher", "ISBN": "123456", "author": "Some Swede", "category":"Fantasy"},
         {"title": "Oliver Twist", "ISBN": "123456", "author": "Charles Dickens", "category":"Fantasy"},
         {"title": "A Christmas Carol", "ISBN": "123456", "author": "Charles Dickens", "category":"Fantasy"},
         {"title": "Cinderally", "ISBN": "123456", "author": "Random", "category":"Folk"},
         {"title": "The Tale Of Two Cities", "ISBN": "123456", "author": "Charles Dickens", "category":"Fantasy"},
         {"title": "War Of The 3 Kingdoms", "ISBN": "123456", "author": "Some Swede", "category":"Romance"},
         {"title": "Lord Of The Rings", "ISBN": "123456", "author": "Tolken", "category":"Fantasy"}]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_all_books(book_title: str):
    """
    Example using path parameter
    """
    books_to_return = []
    for book in BOOKS:
        if (book_title.casefold() in book.get('title').casefold()):
            books_to_return.append(book)
    return books_to_return

@app.get("/books/")
async def read_catgory_by_query(category: str):
    """
    Example using query parameter
    """
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/{author}/")
async def read_author_category_by_query(author: str, category: str):
    """
    Example using query and path parmeter together
    """
    books_to_return = []
    print(author, category)
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold() and book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return

@app.post("/books/create_book")
async def create_book(new_book=Body(None)):
    BOOKS.append(new_book)

@app.put("/books/update_book")
async def update_book(new_book=Body(None)):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == new_book.get('title').casefold():
            BOOKS[i]= new_book

@app.delete("/books/delete_book/{title}")
async def delete_book(title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == title.casefold():
            BOOKS.pop(i)
            break
