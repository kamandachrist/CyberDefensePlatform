from fastapi import APIRouter, Depends, HTTPException, Form

from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.user import UserCreate, UserLogin
from app.services.auth_service import (
    create_user,
    login_user,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    try:
        return create_user(db, user)
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):

    token = login_user(
        db,
        username,
        password,
    )

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
        )

    return token