from fastapi import FastAPI
import uvicorn

app = FastAPI

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

    
books = [
    {
        "id": 1,
        "title": "Колобок",
        "author": "Мэттью",
    },
    {
        "id": 2,
        "title": "Holly Father",
        "author": "Артем",
    },
]

@app.get('/books')
def read_books():
    return books
