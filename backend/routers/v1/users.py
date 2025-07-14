from http.client import HTTPException
from fastapi import APIRouter
from ...schemas import user_schema
from ...models import user_model
from ... import models

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
async def get_users(page=1, size_per_page = 50) -> list[user_model.User]:
    db_users = models.session.exec(
        user_model.User.select().offset((page - 1) * size_per_page).limit(size_per_page)
    ).scalars().all()
    # db_users = models.session.(user_model.User.select().offset((page-1)* size_per_page).limit(size_per_page)).scalars().all()
    return db_users


@router.get("/{account_id}")
async def get_user(user_id: int) -> user_model.User:
    db_user = models.session.get(user_model.User, user_id)
    if not db_user :
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/register")
async def create_user(user: user_model.User) -> user_model.User:
    db_user = user_model.User(**user.model_dump(exclude_unset=True))  # Convert Pydantic model to SQLModel
    models.session.add(db_user)
    models.session.commit()

    return db_user


@router.put("/{user_id}")
async def update_user(user_id: int, user: user_schema.User) -> user_schema.User:
    return user


@router.delete("/delete/{user_id}")
async def delete_user(user_id: int) -> dict:
    return {"message": f"user_schema.User with ID {user_id} has been deleted."}
