from fastapi import *
from fastapi.responses import *
from fastapi.staticfiles import StaticFiles

from database import Base, engine
from routers import courses

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(courses.router)

app.mount("/static", StaticFiles(directory="static", html=True))


@app.get("/", response_class = HTMLResponse)
def health_check():
    return "<p>HElo</p>"

@app.get("/about")
def r():
    return FileResponse("index.html", filename="qwe", media_type="application/octet-stream")

# @app.get("/users/{id}")
# def users(id:int = Path(ge=10, lt=40)):
#     return {"users": id}

@app.get("/users")
def users(people: list[str] = Query()):
    return {"people": people}


@app.get("/notfound", status_code=status.HTTP_404_NOT_FOUND)
def notfound():
    return {"message": "not found"}

@app.get("/old")
def old():
    return RedirectResponse("https://metanit.com/python/fastapi")

@app.get("/new")
def new():
    return "neww"


@app.post("/hello")
def hello(name:str  = Body(embed=True, min_length=3, max_length=20),
            age: int = Body(embed=True, ge=18, lt=111)):
    return {"message": f"{name} тебе {age}"}