from datetime import datetime

from sqlmodel import Field, SQLModel

__all__ = ("Material",)


class Material(SQLModel, table=True):
    id: int = Field(primary_key=True)
    # excel_id = db.Column(db.Integer)
    name: str = Field(nullable=False)
    iron_amount: float = Field(default=0)
    silicon_amount: float = Field(default=0)
    aluminum_amount: float = Field(default=0)
    sodium_amount: float = Field(default=0)
    sulfur_amount: float = Field(default=0)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)