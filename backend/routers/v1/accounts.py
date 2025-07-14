from fastapi import APIRouter
from ...schemas.account_schema import Account

router = APIRouter(prefix="/accounts", tags=["accounts"])


@router.get("/")
async def get_accounts() -> list[Account]:
    return [
        Account(
            id=1,
            fullname="John Doe",
            email="john.doe@example.com",
            phone_number="0812345678",
            id_card="1234567890123",
        ),
        Account(
            id=2,
            fullname="Jane Smith",
            email="jane.smith@example.com",
            phone_number="0898765432",
            id_card="9876543210987",
        ),
    ]


@router.get("/{account_id}")
async def get_account(account_id: int) -> Account:
    return Account(
        id=1,
        fullname="John Doe",
        email="john.doe@example.com",
        phone_number="0812345678",
        id_card="1234567890123",
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
