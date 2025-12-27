from datetime import datetime
from pydantic import BaseModel
from app.schemas.base import ORMBase

class ScrappedEquipmentCreate(BaseModel):
    equipmentId: int

class ScrappedEquipmentRead(ORMBase):
    equipmentId: int
    createdAt: datetime