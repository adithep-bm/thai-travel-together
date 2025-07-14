from fastapi import APIRouter
from ...schemas.user_schema import User

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
async def get_users() -> list[User]:
    return [
        User(
            id=1,
            fullname="John Doe",
            email="john.doe@example.com",
            phone_number="0812345678",
            id_card="1234567890123",
        ),
        User(
            id=2,
            fullname="Jane Smith",
            email="jane.smith@example.com",
            phone_number="0898765432",
            id_card="9876543210987",
        ),
    ]


@router.get("/{account_id}")
async def get_user(user_id: int) -> User:
    return User(
        id=1,
        fullname="John Doe",
        email="john.doe@example.com",
        phone_number="0812345678",
        id_card="1234567890123",
    )


@router.post("/register")
async def create_user(user: User) -> User:
    return user


@router.put("/{user_id}")
async def update_user(user_id: int, user: User) -> User:
    return user


@router.delete("/delete/{user_id}")
async def delete_user(user_id: int) -> dict:
    return {"message": f"User with ID {user_id} has been deleted."}
