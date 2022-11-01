from datetime import datetime
from typing import Optional

from pydantic import BaseModel

__all__ = (
    "MaterialModel",
    "MaterialCreate",
    "MaterialListResponse",
)


class MaterialBase(BaseModel):
    name: str
    iron_amount: Optional[float] = 0
    silicon_amount: Optional[float] = 0
    aluminum_amount: Optional[float] = 0
    sodium_amount: Optional[float] = 0
    sulfur_amount: Optional[float] = 0
    month: str


class MaterialCreate(MaterialBase):
    ...


class MaterialModel(MaterialBase):
    id: int


class MaterialListResponse(BaseModel):
    Materials: list[MaterialModel] = []


class ReportListResponse(BaseModel):
    Materials: list[dict] = []
