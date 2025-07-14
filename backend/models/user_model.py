from sqlmodel import SQLModel, Field
from typing import Optional
from ..schemas import user_schema


class User(SQLModel,user_schema.User , table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    hashed_password: str
    full_name: Optional[str] = None
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)
