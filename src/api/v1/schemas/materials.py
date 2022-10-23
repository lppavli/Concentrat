from datetime import datetime

from pydantic import BaseModel

__all__ = (
    "MaterialModel",
    "MaterialCreate",
    "MaterialListResponse",
)


class MaterialBase(BaseModel):
    name: str
    iron_amount: float
    silicon_amount: float
    aluminum_amount: float
    sodium_amount: float
    sulfur_amount: float


class MaterialCreate(MaterialBase):
    ...


class MaterialModel(MaterialBase):
    id: int
    created_at: datetime


class MaterialListResponse(BaseModel):
    Materials: list[MaterialModel] = []