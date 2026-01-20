from pydantic import BaseModel

# -------- USERS --------
class UserCreate(BaseModel):
    username: str
    password: str


class UserRead(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True


# -------- AUTH --------
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# -------- TODOS --------
class TodoCreate(BaseModel):
    item: str


class TodoRead(BaseModel):
    id: int
    item: str

    class Config:
        from_attributes = True
