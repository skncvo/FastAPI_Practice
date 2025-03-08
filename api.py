# api.py
from fastapi import FastAPI
from todo import todo_router


app = FastAPI()  # 반드시 'app' 변수명 사용

@app.get("/")
async def welcome() -> dict:
    return{
        "message": "hello world!"
    }

app.include_router(todo_router)
