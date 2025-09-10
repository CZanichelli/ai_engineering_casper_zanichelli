from fastapi import FastAPI, Query
from data_processing import library_data, Book
from constants import CURRENT_YEAR

app = FastAPI()

library = library_data("library.json")
books = library.books



@app.get("/books")
async def read_books():
    return books

# path parameter
@app.get("/books/title/{title}")
async def read_book_by_title(title: str):
    return [book for book in books if book.title.casefold() == title.casefold()]


@app.post("/books/create_book")
async def create_book(book_request: Book):
    new_book = Book.model_validate(book_request)
    books.append(new_book)

    return new_book

# TODO: 
# update
@app.put("/books/update_book")
async def update_book(updated_book: Book):
    for i, book in enumerate(books):
        if book.id == updated_book.id:
            books[i] = updated_book
    return updated_book



# delete
@app.delete("/books/delete_book/{id}")
async def delete_book(id: int):
    for i, book in enumerate(books):
        if book.id == id:
            del books[i]
            break


# query parameters
@app.get("/books/")
async def filter_books(
    start_year: int = Query(
        1950,
        gt=1500,
        lt= CURRENT_YEAR + 1,
        description="Filters books that are newer than this year"
        
    ),
    end_year: int = Query(
        CURRENT_YEAR,
        gt=1500,
        lt= CURRENT_YEAR + 1,
        description="Filters books that are older than this year"
        
    ),
    author: str=Query(None,description="Authors firstname and lastname "),
):
    filterd_books = [book for book in books if start_year < book.year and end_year > book.year]

    if author: 
        filterd_books = [
        book
        for book in filterd_books
        if author.casefold() == book.author.casefold() 
    ]
    return filterd_books

