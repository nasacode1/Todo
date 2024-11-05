from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TodoBase(BaseModel):
    name: str
    description: Optional[str]=None

class TodoCreate(TodoBase):
    pass  
class TodoResponse(TodoBase):
    id: int
    name: str
    date_created: datetime
    class Config:
        orm_mode = True  
