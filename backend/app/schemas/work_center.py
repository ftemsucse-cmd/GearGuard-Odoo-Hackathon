from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from app.schemas.base import ORMBase

class WorkCenterCreate(BaseModel):
    name: str

class WorkCenterUpdate(BaseModel):
    name: Optional[str] = None

class WorkCenterRead(ORMBase):
    id: int
    name: str
    createdAt: datetime
    updatedAt: datetime