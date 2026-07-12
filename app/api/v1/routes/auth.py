from app.utils.security import hash_password
from app.schemas.login import UserLogin
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import UserRegister
from app.models.user import User
from app.database import get_db
from app.schemas.login import UserLogin
router = APIRouter()

@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    
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
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()

    return users
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

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

    return {
        "message": "Login successful",
        "user_id": existing_user.id,
        "name": existing_user.name,
        "email": existing_user.email
    }