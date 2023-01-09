from sqlalchemy import Time, Column, Date, Integer, String, Text

from config.database import Base, engine


class TodoTask(Base):
    __tablename__ = "todo_task"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title = Column(String(255))
    description = Column(Text, nullable=True)
    date = Column(Date)
    time = Column(Time)


Base.metadata.create_all(bind=engine)
