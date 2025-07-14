from fastapi import APIRouter
from ...schemas import user_schema
from ...models import user_model
from ... import models

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
async def get_users() -> list[user_schema.User]:
    return [
        user_schema.User(
            id=1,
            fullname="John Doe",
            email="john.doe@example.com",
            phone_number="0812345678",
            id_card="1234567890123",
        ),
        user_schema.User(
            id=2,
            fullname="Jane Smith",
            email="jane.smith@example.com",
            phone_number="0898765432",
            id_card="9876543210987",
        ),
    ]


@router.get("/{account_id}")
async def get_user(user_id: int) -> user_model.User:
    db_user = models.session.get(user_model.User, user_id)
    if db_user is None:
        return user_schema.User(
            id=None,
            fullname="Not Found",
            email="Not Found",
        )
    return db_user


@router.post("/register")
async def create_user(user: user_schema.User) -> user_model.User:
    db_user = user_model.user_schema.User(**user.model_dump(exclude_unset=True))  # Convert Pydantic model to SQLModel
    models.session.add(db_user)
    models.session.commit()

    return db_user


@router.put("/{user_id}")
async def update_user(user_id: int, user: user_schema.User) -> user_schema.User:
    return user


@router.delete("/delete/{user_id}")
async def delete_user(user_id: int) -> dict:
    return {"message": f"user_schema.User with ID {user_id} has been deleted."}
