from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session

from app.schemas.user import UserRegister, UserUpdate
from app.schemas.login import UserLogin
from app.models.user import User
from app.database import get_db
from app.utils.security import hash_password
from app.utils.jwt_handler import (
    create_access_token,
    verify_access_token
)

router = APIRouter()


@router.post("/register")
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):
    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "user_id": new_user.id
    }


@router.get("/users")
def get_users(
    db: Session = Depends(get_db)
):
    users = db.query(User).all()
    return users


@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not existing_user:
        return {
            "message": "Invalid email or password"
        }

    if existing_user.password != user.password:
        return {
            "message": "Invalid email or password"
        }

    access_token = create_access_token(
        {
            "sub": existing_user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.put("/users/{user_id}")
def update_user(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not existing_user:
        return {
            "message": "User not found"
        }

    existing_user.name = user_data.name
    existing_user.email = user_data.email

    db.commit()
    db.refresh(existing_user)

    return {
        "message": "User updated successfully",
        "user": {
            "id": existing_user.id,
            "name": existing_user.name,
            "email": existing_user.email
        }
    }


@router.get("/me")
def get_me(
    authorization: str = Header(None),
    db: Session = Depends(get_db)
):
    if not authorization:
        return {
            "message": "Authorization header missing"
        }

    token = authorization.replace(
        "Bearer ",
        ""
    )

    payload = verify_access_token(token)

    if not payload:
        return {
            "message": "Invalid or expired token"
        }

    email = payload.get("sub")

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        return {
            "message": "User not found"
        }

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }
from sqlalchemy.orm import Session

from app.schemas.user import UserRegister, UserUpdate
from app.schemas.login import UserLogin
from app.models.user import User
from app.database import get_db
from app.utils.security import hash_password
from app.utils.jwt_handler import (
    create_access_token,
    verify_access_token
)

router = APIRouter()


@router.post("/register")
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):
    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "user_id": new_user.id
    }


@router.get("/users")
def get_users(
    db: Session = Depends(get_db)
):
    users = db.query(User).all()
    return users


@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not existing_user:
        return {
            "message": "Invalid email or password"
        }

    if existing_user.password != user.password:
        return {
            "message": "Invalid email or password"
        }

    access_token = create_access_token(
        {
            "sub": existing_user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.put("/users/{user_id}")
def update_user(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not existing_user:
        return {
            "message": "User not found"
        }

    existing_user.name = user_data.name
    existing_user.email = user_data.email

    db.commit()
    db.refresh(existing_user)

    return {
        "message": "User updated successfully",
        "user": {
            "id": existing_user.id,
            "name": existing_user.name,
            "email": existing_user.email
        }
    }


@router.get("/me")
def get_me(
    authorization: str = Header(None),
    db: Session = Depends(get_db)
):
    if not authorization:
        return {
            "message": "Authorization header missing"
        }

    token = authorization.replace(
        "Bearer ",
        ""
    )

    payload = verify_access_token(token)

    if not payload:
        return {
            "message": "Invalid or expired token"
        }

    email = payload.get("sub")

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        return {
            "message": "User not found"
        }

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }