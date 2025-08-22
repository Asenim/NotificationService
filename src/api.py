from fastapi import APIRouter, Depends
from src.rest_models import UserCreate, User
from src.db_services import UserRepository


router = APIRouter()


@router.post("/register", response_model=User)
async def register(user: UserCreate, repo: UserRepository = Depends()):
    return await repo.create_user(username=user.username)
