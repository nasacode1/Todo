from fastapi import FastAPI
from database import engine
from database import Base
import schemas

Base.metadata.create_all(bind=engine)
app = FastAPI()

from fastapi import Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import crud

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/todos/", response_model=schemas.TodoResponse)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db=db, todo=todo)