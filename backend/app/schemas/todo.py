from pydantic import BaseModel

class TodoCreate(BaseModel):
    item: str

class TodoRead(BaseModel):
    id: int
    item: str

    class Config:
        orm_mode = True  # Allows SQLAlchemy objects to be returned
