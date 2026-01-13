from app.core.database import engine
from app.models import Todo
from app.core.database import Base

Base.metadata.create_all(bind=engine)
