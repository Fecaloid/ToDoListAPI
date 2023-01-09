import datetime

from dateutil.relativedelta import relativedelta

from utils.functions import change_time

now = datetime.datetime.utcnow()
today = now.date()
yesterday = (now - relativedelta(days=1)).date()
test_time = datetime.datetime(now.year, now.month, now.day, 15, 30)


todo_task_list = [
    {
        "title": "Test task 1",
        "description": "Test task 1 description",
        "date": str(today),
        "time": str(change_time(test_time))
    },
    {
        "title": "Test task 2",
        "description": "Test task 2 description",
        "date": str(today),
        "time": str(change_time(test_time, hours=1))
    },
    {
        "title": "Test task 3",
        "description": "Test task 3 description",
        "date": str(today),
        "time": str(change_time(test_time, hours=2))
    },
    {
        "title": "Test task 4",
        "description": "Test task 4 description",
        "date": str(yesterday),
        "time": str(change_time(test_time))
    },
    {
        "title": "Test task 5",
        "description": "Test task 5 description",
        "date": str(yesterday),
        "time": str(change_time(test_time, hours=1))
    },
]
