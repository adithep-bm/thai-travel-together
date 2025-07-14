from sqlmodel import SQLModel, Field
from typing import Optional
from ..schemas import province_schema


class Province(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    province_state: province_schema.Province_state = Field(
        default=province_schema.Province_state.primary
    )
