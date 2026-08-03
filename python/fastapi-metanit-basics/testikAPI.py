from fastapi import *
from fastapi.responses import *
from fastapi.staticfiles import StaticFiles

from pydantic import BaseModel, Field

app = FastAPI()


class Good(BaseModel):
    name: str
    price: int = Field(gt=0)


class Order(BaseModel):
    adress: str
    goods: list[Good]


@app.post("/orders")
def order(order: Order):
    sumgoods = 0
    for good in order.goods:
        sumgoods += good.price
        
    return {
        "адресс": order.adress,
        "товары": order.goods,
        "общцена": sumgoods,
    }


# class Company(BaseModel):
#     name: str = Field(ge=4)

# class Person(BaseModel):
#     name: str = Field(min_length=3, max_length=20)
#     age: int | None = Field(ge=18)
#     company: Company | None = None

# app.mount("/static", StaticFiles(directory="static", html=True))


# @app.get("/", response_class = HTMLResponse)
# def health_check():
#     return FileResponse("static/index.html")


# @app.post("/hello")
# def hello(person: Person):
#     return {"message": f"{person.name} тебе {person.age}"}
#####################################################33
# @app.get("/about")
# def r():
#     return FileResponse("index.html", filename="qwe", media_type="application/octet-stream")

# # @app.get("/users/{id}")
# # def users(id:int = Path(ge=10, lt=40)):
# #     return {"users": id}

# @app.get("/users")
# def users(people: list[str] = Query()):
#     return {"people": people}


# @app.get("/notfound", status_code=status.HTTP_404_NOT_FOUND)
# def notfound():
#     return {"message": "not found"}

# @app.get("/old")
# def old():
#     return RedirectResponse("https://metanit.com/python/fastapi")

# @app.get("/new")
# def new():
#     return "neww"


# @app.post("/hello")
# def hello(name:str  = Body(embed=True, min_length=3, max_length=20),
#             age: int = Body(embed=True, ge=18, lt=111)):
#     return {"message": f"{name} тебе {age}"}
