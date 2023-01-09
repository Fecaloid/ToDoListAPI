import datetime

from pydantic import BaseModel


class TodoTaskBase(BaseModel):
    title: str
    description: str | None = None
    date: datetime.date
    time: datetime.time


class TodoTask(TodoTaskBase):
    id: int
    completed: bool

    class Config:
        orm_mode = True
