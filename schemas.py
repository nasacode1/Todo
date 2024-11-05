from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TodoBase(BaseModel):
    name: str
    description: Optional[str]=None
    due_date: Optional
class TodoCreate(TodoBase):
    pass  # No additional fields needed for creation

class TodoResponse(TodoBase):
    id: int
    created_at: datetime
    completed: bool

    class Config:
        orm_mode = True  # Allow compatibility with ORM models
