from fastapi import FastAPI

from apps.todo_task.route import router as todo_task_router

app = FastAPI()

app.include_router(todo_task_router)
