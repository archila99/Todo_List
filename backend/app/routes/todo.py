from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.deps import get_db
from app.auth.dependencies import get_current_user
from app.models import Todo
from app.schemas.schemas import TodoCreate, TodoRead

router = APIRouter(prefix="/todos", tags=["Todos"])

@router.get("/", response_model=list[TodoRead])
def get_todos(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return (
        db.query(Todo)
        .filter(Todo.user_id == current_user.id)
        .all()
    )


@router.get("/{todo_id}", response_model=TodoRead)
def get_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    todo = (
        db.query(Todo)
        .filter(Todo.id == todo_id, Todo.user_id == current_user.id)
        .first()
    )

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    return todo


@router.post("/", response_model=TodoRead)
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    db_todo = Todo(
        item=todo.item,
        user_id=current_user.id
    )

    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)

    return db_todo


@router.put("/{todo_id}", response_model=TodoRead)
def update_todo(
    todo_id: int,
    todo: TodoCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    db_todo = (
        db.query(Todo)
        .filter(Todo.id == todo_id, Todo.user_id == current_user.id)
        .first()
    )

    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    db_todo.item = todo.item
    db.commit()
    db.refresh(db_todo)

    return db_todo


@router.delete("/{todo_id}")
def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    db_todo = (
        db.query(Todo)
        .filter(Todo.id == todo_id, Todo.user_id == current_user.id)
        .first()
    )

    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(db_todo)
    db.commit()

    return {"message": "Todo deleted successfully"}
