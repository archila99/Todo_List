from database import Base, engine
from models import Todo

Base.metadata.create_all(bind=engine)