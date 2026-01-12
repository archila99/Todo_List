from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Todo
from schemas import TodoCreate, TodoRead

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# get all todos 
@app.get("/todos", response_model=list[TodoRead])
def get_todos(db: Session = Depends(get_db)):
    return db.query(Todo).all()

# get single todo 
@app.get("/todos/{todo_id}", response_model=TodoRead)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo
    
# create a todo 
@app.post("/todos", response_model=TodoRead)
def create_todos(todo: TodoCreate, db: Session= Depends(get_db)):
    db_todo = Todo(item=todo.item)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

# update a todo 
@app.put("/todos/{todo_id}", response_model=TodoRead)
def update_todo(todo_id: int, todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db_todo.item = todo.item
    db.commit()
    db.refresh(db_todo)
    return db_todo

# delete a todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    return {"message": "Todo deleted successfully"}
    
