from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user_models import User
from app.schemas.auth_schema import Token
from app.services.auth_service import (
    create_access_token,
    verify_password,
    get_current_user
)

router = APIRouter(tags=["auth"])



@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=400,
            detail="نام کاربری یا رمز عبور اشتباه است"
        )
    if not user.is_active:
        raise HTTPException(
            status_code=403,
            detail="کاربر غیرفعال است"
        )
    token = create_access_token({"sub": user.username, "role": user.role.name if user.role else ""})
    return {"access_token": token, "token_type": "bearer"}



@router.get("/me")
def me(
    current_user: User = Depends(get_current_user)
):

    if current_user.role.name in ["ADMIN", "ADMINISTRATOR"]:

        return {
            "username": current_user.username,
            "role": current_user.role.name,
            "companies": []
        }

    return {
        "username": current_user.username,
        "role": current_user.role.name,
        "companies": [
            c.company_name
            for c in current_user.companies
        ]
    }
