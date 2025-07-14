from pydantic import BaseModel


class User(BaseModel):
    id: int
    fullname: str
    email: str
    phone_number: str
    id_card: str
