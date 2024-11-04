from fastapi import FastAPI
from database import engine
from database import Base

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