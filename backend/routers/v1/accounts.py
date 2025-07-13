from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
import decimal

router = APIRouter(prefix="/accounts", tags=["accounts"])


class Account(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    phone_number: str
    id_card: str
    laser_number: str
    address: str
    birth_date: datetime


@router.get("/")
async def get_accounts() -> list[Account]:
    return [
        Account(
            id=1,
            name="John",
            surname="Doe",
            email="john.doe@example.com",
            phone_number="0812345678",
            id_card="1234567890123",
            laser_number="ABC123456789",
            address="123 Main St, Bangkok",
            birth_date=datetime(1990, 1, 1),
        ),
        Account(
            id=2,
            name="Jane",
            surname="Smith",
            email="jane.smith@example.com",
            phone_number="0898765432",
            id_card="9876543210987",
            laser_number="XYZ987654321",
            address="456 Second St, Chiang Mai",
            birth_date=datetime(1985, 5, 15),
        ),
    ]


@router.get("/{account_id}")
async def get_account(account_id: int) -> Account:
    return Account(
        id=1,
        name="John",
        surname="Doe",
        email="john.doe@example.com",
        phone_number="0812345678",
        id_card="1234567890123",
        laser_number="ABC123456789",
        address="123 Main St, Bangkok",
        birth_date=datetime(1990, 1, 1),
    )


@router.post("/")
async def create_account(account: Account) -> Account:
    return account


@router.put("/{account_id}")
async def update_account(account_id: int, account: Account) -> Account:
    return account


@router.delete("/{account_id}")
async def delete_account(account_id: int) -> dict:
    return {"message": f"Account with ID {account_id} has been deleted."}
