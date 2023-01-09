from sqlalchemy import Time, Column, Date, Integer, String, Text, BOOLEAN

from config.database import Base, engine


class TodoTask(Base):
    __tablename__ = "todo_task"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    completed = Column(BOOLEAN, nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)


Base.metadata.create_all(bind=engine)
