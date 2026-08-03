from fastapi import FastAPI, Header, Cookie, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

tasks_db = []
current_id = 1

class TaskCreate(BaseModel):
    subject: str
    text: str
    answer: str

class Task(BaseModel):
    task_id: int
    subject: str
    text: str
    answer: str



from fastapi import FastAPI, Response, Cookie

app = FastAPI()

@app.post("/set-cookie")
def set_cookie(response: Response):
    response.set_cookie(key="my_test_cookie", value="super_secret_value")
    return {"message": "Кука успешно установлена!"}



@app.get("/get-cookie")
def read_cookie(my_test_cookie: str | None = Cookie(default=None)):
    if my_test_cookie is None:
        return {"message": "Куков нет, ты кто?"}
    return {"Твоя сохраненная кука": my_test_cookie}




@app.post("/login")
def login(
    username: str = Form(), 
    password: str = Form(min_length=6) 
):
    return {
        "логин": username,
        "статус": "Успешно зашел через форму!"
    }



@app.get("/headres")
def get_browser_info(user_agent: str | None = Header(default=None)):
    return {"Your browser": user_agent}

@app.get("/tasks")
def get_all_tasks():
    return tasks_db

@app.post("/tasks")
def create_new_task(task_in: TaskCreate):
    global current_id
    
    new_task = Task(
        task_id=current_id,
        subject=task_in.subject,
        text=task_in.text,
        answer=task_in.answer
    )
    
    tasks_db.append(new_task)
    current_id += 1
    
    return new_task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_in: TaskCreate):
    for i in range(len(tasks_db)):
        if tasks_db[i].task_id == task_id:

            updated_task = Task(
                task_id=task_id,
                subject=task_in.subject,
                text=task_in.text,
                answer=task_in.answer
            )
            tasks_db[i] = updated_task
            return {
                "message": "Task updated successfully", 
                "task": updated_task
            }
            
    return JSONResponse(
        status_code=404,
        content={"message": "Task not found"}
    )

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks_db:
        if task.task_id == task_id:
            tasks_db.remove(task)
            return {
                "message": "Task deleted successfully", 
                "updated_list": tasks_db
            }
            
    return JSONResponse(
        status_code=404,
        content={"message": "Task not found"}
    )