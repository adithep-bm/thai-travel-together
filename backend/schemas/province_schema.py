from pydantic import BaseModel
from enum import Enum

class Province_state(str, Enum):
    primary = "primary"
    secondary = "secondary"


class Province(BaseModel):
    id: int
    name: str
    secondary_province: Province_state
