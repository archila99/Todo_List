from fastapi import FastAPI
from models import Todo

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

todos = []

# get all todos 
@app.get("/todos")
def get_todos():
    return todos

# get single todo 
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "No todo found"}
    
# create a todo 
@app.post("/todos")
def create_todos(todo: Todo):
    todos.append(todo)
    return {"meessage": "Successful"}

# update a todo 
@app.put("/todos/{todo_id}")
def update_todos(todo_id: int, todo_obj: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            return {"todo": todo}
    return {"message": "No todo found to update"}

# delete a todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Todo item has been deleted"}
    return {"message": "No todo found to delete"}
    
