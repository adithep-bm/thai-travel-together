from sqlmodel import SQLModel, Field
from typing import Optional
from ..schemas import user_schema


class User(SQLModel, user_schema.User, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    fullname: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    phone_number: str = Field(index=True, unique=True)
    id_card: str = Field(index=True, unique=True)