from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session

from apps.todo_task import schemas
from apps.todo_task.models import TodoTask


def create_todo_task(db: Session, todo_task: schemas.TodoTaskBase):
    db_todo_task = TodoTask(**todo_task.dict(), completed=False)
    db.add(db_todo_task)
    db.commit()
    db.refresh(db_todo_task)
    return db_todo_task


def get_todo_task(db: Session, todo_task_id: int):
    return db.query(TodoTask).filter(TodoTask.id == todo_task_id).first()


def get_todo_tasks(db: Session, skip: int = 0, limit: int = 100, date: str | None = None):
    qs = db.query(TodoTask)
    if date:
        try:
            qs = qs.where(TodoTask.date == datetime.strptime(date, "%Y-%m-%d").date())
        except ValueError:
            raise HTTPException(status_code=400, detail="Wrong date format. It should be YYYY-MM-DD")
    qs = qs.offset(skip).limit(limit).all()
    return qs


def update_todo_task(db: Session, todo_task_id: int, todo_task: schemas.TodoTaskBase):
    db_todo_task = db.query(TodoTask).filter(TodoTask.id == todo_task_id).one_or_none()
    if not db_todo_task:
        raise HTTPException(status_code=404, detail="Todo task not found")

    todo_task_data = todo_task.dict(exclude_unset=True)
    for key, value in todo_task_data.items():
        setattr(db_todo_task, key, value)

    db.add(db_todo_task)
    db.commit()
    db.refresh(db_todo_task)
    return db_todo_task


def complete_todo_task(db: Session, todo_task_id: int):
    db_todo_task = db.query(TodoTask).filter(TodoTask.id == todo_task_id).one_or_none()
    if not db_todo_task:
        raise HTTPException(status_code=404, detail="Todo task not found")

    setattr(db_todo_task, 'completed', not db_todo_task.completed)
    db.add(db_todo_task)
    db.commit()
    db.refresh(db_todo_task)
    return db_todo_task


def delete_todo_task(db: Session, todo_task_id: int):
    db_todo_task = db.query(TodoTask).filter(TodoTask.id == todo_task_id).one_or_none()
    if not db_todo_task:
        raise HTTPException(status_code=404, detail="Todo task not found")

    db.delete(db_todo_task)
    db.commit()
