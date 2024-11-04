from sqlalchemy import Column, Integer, String, DateTime, Boolean
from .database import Base
from datetime import datetime

class ToDo(Base):
    __tablename__= "todos"

     id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    date_created = Column(DateTime, default=datetime.utcnow)
    date_to_be_completed = Column(DateTime, nullable=True)
    is_important = Column(Boolean, default=False)
