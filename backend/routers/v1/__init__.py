from fastapi import APIRouter
from . import users, provinces

router = APIRouter(prefix="/v1")
router.include_router(users.router)
router.include_router(provinces.router)