from random import choice

from config.test_db import client
from tests.fixtures.todo_task import todo_task_list


def test_create_todo_tasks():
    """
    Case: create many todo_task objects.
    Expect: process finished success.
    """
    for todo_task in todo_task_list:
        response = client.post("/todo_task/", json=todo_task)
        assert response.status_code == 200
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


def test_read_todo_task():
    """
    Case: create and get todo_task.
    Expect: process finished success.
    """
    request = choice(todo_task_list)
    response = client.post("/todo_task/", json=request)
    assert response.status_code == 200
    data = response.json()
    assert data['title'] == request['title']
    assert data['description'] == request['description']
    response = client.get(f"/todo_task/{data['id']}/")
    assert response.status_code == 200
    assert data == response.json()


# def test_read_item():
#     response = client.get("/todo_task/")
#     assert response.status_code == 200
#     b = todo_task_list
#     a = response.json()
#     assert response.json() == {
#         "id": "foo",
#         "title": "Foo",
#         "description": "There goes my hero",
#     }


# def test_read_item_bad_token():
#     response = client.get("/items/foo", headers={"X-Token": "hailhydra"})
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Invalid X-Token header"}
#
#
# def test_read_inexistent_item():
#     response = client.get("/items/baz", headers={"X-Token": "coneofsilence"})
#     assert response.status_code == 404
#     assert response.json() == {"detail": "Item not found"}
#
#
# def test_create_item():
#     response = client.post(
#         "/items/",
#         headers={"X-Token": "coneofsilence"},
#         json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},
#     )
#     assert response.status_code == 200
#     assert response.json() == {
#         "id": "foobar",
#         "title": "Foo Bar",
#         "description": "The Foo Barters",
#     }
#
#
# def test_create_item_bad_token():
#     response = client.post(
#         "/items/",
#         headers={"X-Token": "hailhydra"},
#         json={"id": "bazz", "title": "Bazz", "description": "Drop the bazz"},
#     )
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Invalid X-Token header"}
#
#
# def test_create_existing_item():
#     response = client.post(
#         "/items/",
#         headers={"X-Token": "coneofsilence"},
#         json={
#             "id": "foo",
#             "title": "The Foo ID Stealers",
#             "description": "There goes my stealer",
#         },
#     )
#     assert response.status_code == 400
#     assert response.json() == {"detail": "Item already exists"}