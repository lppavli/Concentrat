from sqlmodel import Field, SQLModel

__all__ = ("Material",)


class Material(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(nullable=False)
    iron_amount: float = Field(default=0, nullable=True)
    silicon_amount: float = Field(default=0, nullable=True)
    aluminum_amount: float = Field(default=0, nullable=True)
    sodium_amount: float = Field(default=0, nullable=True)
    sulfur_amount: float = Field(default=0, nullable=True)
    month: str = Field(nullable=False)
