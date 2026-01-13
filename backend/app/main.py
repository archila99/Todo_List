from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.todo import router as todo_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(todo_router, prefix="/todos", tags=["todos"])
