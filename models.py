from fastapi import FastAPI
from pydantic import BaseModel

class Todo(BaseModel):
    id: int 
    item: str

todo = Todo(id="123", item="ali")
print(todo)
print(todo.id, type(todo.id))
print(todo.item, type(todo.item))