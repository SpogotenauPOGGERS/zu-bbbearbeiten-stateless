from dataclasses import dataclass
import datetime

todos = []


@dataclass
class Todo:
    title: str
    date: datetime.date 
    isCompleted: bool = False


def add(title, date):
    title = title.replace('b', 'bbb').replace('B', 'Bbb') # frage 1d
    
    todos.append(Todo(title, date))


def get_all():
    return todos


def get(index):
    return todos[index]


def update(index):
    todos[index].isCompleted = not todos[index].isCompleted
