from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security.password import (
    hash_password,
    verify_password,
)
from app.core.security.jwt import create_access_token


def get_user_by_username(
    db: Session,
    username: str,
) -> User | None:
    return (
        db.query(User)
        .filter(User.username == username)
        .first()
    )


def create_user(
    db: Session,
    user: UserCreate,
) -> User:

    existing = get_user_by_username(
        db,
        user.username,
    )

    if existing:
        raise ValueError("Username already exists")

    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password),
        full_name=user.full_name,
        role="analyst",
        is_active=True,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def authenticate_user(
    db: Session,
    username: str,
    password: str,
):

    user = get_user_by_username(
        db,
        username,
    )

    if not user:
        return None

    if not verify_password(
        password,
        user.hashed_password,
    ):
        return None

    return user


def login_user(
    db: Session,
    username: str,
    password: str,
):

    user = authenticate_user(
        db,
        username,
        password,
    )

    if not user:
        return None

    token = create_access_token(
        {
            "sub": user.username,
            "role": user.role,
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }