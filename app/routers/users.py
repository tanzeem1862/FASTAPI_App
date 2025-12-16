from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas import UserCreate, UserResponse, UserCreateResponse
from app.crud import create_user, get_users

router = APIRouter()

@router.post("/users", response_model=UserCreateResponse)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = create_user(db, user)
        return {
            "message": "User created successfully",
            "user": {
                "name": db_user.name,
                "email": db_user.email
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/users", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    users = get_users(db)
    return users