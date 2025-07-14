from pydantic import BaseModel
from enum import Enum

class Province_state(str, Enum):
    primary = "primary"
    secondary = "secondary"


class Province(BaseModel):
    name: str
    province_state: Province_state
