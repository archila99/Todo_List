from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.deps import get_db
from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoRead

router = APIRouter()

@router.get("/", response_model=list[TodoRead])
def get_todos(db: Session = Depends(get_db)):
    return db.query(Todo).all()

@router.get("/{todo_id}", response_model=TodoRead)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.post("/", response_model=TodoRead)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = Todo(item=todo.item)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@router.put("/{todo_id}", response_model=TodoRead)
def update_todo(todo_id: int, todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    db_todo.item = todo.item
    db.commit()
    db.refresh(db_todo)
    return db_todo

@router.delete("/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(db_todo)
    db.commit()
    return {"message": "Todo deleted successfully"}
