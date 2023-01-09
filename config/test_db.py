from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from config.database import Base, get_db
from main import app

SQLALCHEMY_DATABASE_URL = "postgresql://todo_list_user:todo_list_pass@tdl_test_postgres:5432/todo_list_test_db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)
