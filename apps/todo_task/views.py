from datetime import datetime

from sqlalchemy.orm import Session

from apps.todo_task import schemas
from apps.todo_task.models import TodoTask


def get_todo_task(db: Session, todo_task_id: int):
    return db.query(TodoTask).filter(TodoTask.id == todo_task_id).first()


def get_todo_tasks(db: Session, skip: int = 0, limit: int = 100, date: str | None = None):
    qs = db.query(TodoTask)
    print(date)
    if date:
        qs = qs.where(TodoTask.date <= datetime.strptime(date, "%Y-%m-%d").date())
    qs = qs.offset(skip).limit(limit).all()
    return qs


def create_todo_task(db: Session, todo_task: schemas.TodoTaskBase):
    db_item = TodoTask(**todo_task.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
