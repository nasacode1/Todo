from sqlalchemy.orm import Session
from models import Todo
from schemas import TodoCreate

def create_todo(db: Session, todo: TodoCreate):
    db_todo= Todo(name=todo.name, description=todo.description, date_to_be_completed=todo.due_date)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_todos(db: Session):
    return db.query(Todo).all()

