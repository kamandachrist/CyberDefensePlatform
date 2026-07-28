from fastapi import APIRouter, Depends

from app.models.user import User
from app.core.security.dependencies import get_current_user


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/me")
def read_current_user(
    current_user: User = Depends(get_current_user),
):

    return {
        "username": current_user.username,
        "email": current_user.email,
        "role": current_user.role,
    }