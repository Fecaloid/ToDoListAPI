from apps.todo_task import schemas, views
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi import APIRouter

from config.database import get_db

router = APIRouter()


@router.post("/todo_task/", response_model=schemas.TodoTask)
def create_todo_task(todo_task: schemas.TodoTaskBase, db: Session = Depends(get_db)):
    return views.create_todo_task(db=db, todo_task=todo_task)


@router.get("/todo_task/", response_model=list[schemas.TodoTask])
def read_todo_tasks(offset: int = 0, limit: int = 100, db: Session = Depends(get_db), date: str | None = None):
    todo_tasks = views.get_todo_tasks(db, skip=offset, limit=limit, date=date)
    print(todo_tasks)
    return todo_tasks


@router.get("/todo_task/{todo_task_id}/", response_model=schemas.TodoTask)
def read_todo_task(todo_task_id: int, db: Session = Depends(get_db)):
    todo_task = views.get_todo_task(db, todo_task_id=todo_task_id)
    if todo_task is None:
        raise HTTPException(status_code=404, detail="Todo task not found")
    return todo_task
