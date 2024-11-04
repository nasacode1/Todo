from sqlalchemy.orm import Session
from models import Todo

def get_todos(db: Session):
    return db.query(Todo).all()

