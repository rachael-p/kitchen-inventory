from pydantic import BaseModel, HttpUrl, field_validator
from typing import Optional, List

def validate_name(val: str) -> str:
    if not val or not val.strip():
        raise ValueError("Name cannot be empty")
    return val

class Item(BaseModel):
    id: int
    name: str
    price: Optional[float] = None
    link: Optional[HttpUrl] = None

class ItemInput(BaseModel):
    name: str
    price: Optional[float] = None
    link: Optional[HttpUrl] = None

    @field_validator("name")
    @classmethod
    def name_not_empty(cls, val):
        return validate_name(val)

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    link: Optional[HttpUrl] = None

    @field_validator("name")
    @classmethod
    def name_not_empty(cls, val):
        if val is not None:
            return validate_name(val)
        return val

class ItemsResponse(BaseModel):
    count: int
    items: List[Item]