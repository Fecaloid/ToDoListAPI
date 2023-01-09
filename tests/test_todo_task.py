from random import choice

from config.test_db import client
from tests.fixtures.todo_task import todo_task_list, today


def test_create_todo_tasks():
    """
    Case: create many todo_task objects.
    Expect: process finished success.
    """
    for todo_task in todo_task_list:
        response = client.post("/todo_task/", json=todo_task)
        assert response.status_code == 201
        data = response.json()
        assert data['title'] == todo_task['title']
        assert data['description'] == todo_task['description']


def test_read_todo_tasks():
    """
    Case: read todo_tasks with filters.
    Expect: process finished success.
    """
    response = client.get('/todo_task/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(todo_task_list)

    response = client.get(f'/todo_task/?date={today}')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3


def test_read_todo_task():
    """
    Case: create and get todo_task.
    Expect: process finished success.
    """
    request = choice(todo_task_list)
    response = client.post("/todo_task/", json=request)
    assert response.status_code == 201
    data = response.json()
    assert data['title'] == request['title']
    assert data['description'] == request['description']
    response = client.get(f"/todo_task/{data['id']}/")
    assert response.status_code == 200
    assert data == response.json()


def test_update_todo_task():
    """
    Case: create, update and get todo_task.
    Expect: process finished success.
    """
    request = choice(todo_task_list)
    response = client.post("/todo_task/", json=request)
    assert response.status_code == 201
    data = response.json()
    assert data['title'] == request['title']
    request['title'] = 'modified'
    response = client.put(f"/todo_task/{data['id']}/", json=request)
    assert response.status_code == 200
    data = response.json()
    assert data['title'] == 'modified'


def test_complete_todo_task():
    """
    Case: create, complete and get todo_task.
    Expect: process finished success.
    """
    request = choice(todo_task_list)
    response = client.post("/todo_task/", json=request)
    assert response.status_code == 201
    data = response.json()
    assert data['title'] == request['title']
    response = client.patch(f"/todo_task/{data['id']}/")
    assert response.status_code == 200
    data = response.json()
    assert data['completed']


def test_delete_todo_task():
    """
    Case: create, complete and get todo_task.
    Expect: process finished success.
    """
    request = choice(todo_task_list)
    response = client.post("/todo_task/", json=request)
    assert response.status_code == 201
    data = response.json()
    assert data['title'] == request['title']
    response = client.delete(f"/todo_task/{data['id']}/")
    assert response.status_code == 204
    response = client.get(f"/todo_task/{data['id']}/")
    assert response.status_code == 404


def test_failed_create_todo_task():
    """
    Case: try to create task with wrong data.
    Expect: process failed.
    """
    request = choice(todo_task_list).copy()
    del request['title']
    response = client.post("/todo_task/", json=request)
    assert response.status_code == 422

    request = choice(todo_task_list).copy()
    del request['date']
    response = client.post("/todo_task/", json=request)
    assert response.status_code == 422

    request = choice(todo_task_list).copy()
    del request['time']
    response = client.post("/todo_task/", json=request)
    assert response.status_code == 422
