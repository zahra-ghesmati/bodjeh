from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.user_models import (
    User,
    Role,
    UserCompany
)

from app.schemas.user_schema import (
    UserCreate,
    UserUpdate
)

from app.services.auth_service import (
    get_password_hash,
    get_current_user
)

router = APIRouter(
    prefix="/api/users",
    tags=["Users"]
)

COMPANIES = [
    "سيمان مازندران",
    "گروه صنايع سيمان کرمان",
    "بين المللي ساروج بوشهر",
    "سيمان شمال",
    "توليدي سيمان فيروزکوه"
]


def require_administrator(
    current_user: User = Depends(
        get_current_user
    )
):

    if (
        current_user.role.name
        != "ADMINISTRATOR"
    ):

        raise HTTPException(
            status_code=403,
            detail="دسترسی غیرمجاز"
        )

    return current_user


# =========================
# Meta
# =========================

@router.get("/meta/roles")
def get_roles(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_administrator
    )
):

    roles = db.query(Role).all()

    return [
        {
            "id": role.id,
            "name": role.name
        }
        for role in roles
    ]


@router.get("/meta/companies")
def get_companies(
    current_user: User = Depends(
        require_administrator
    )
):

    return COMPANIES


# =========================
# List Users
# =========================

@router.get("")
def get_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_administrator
    )
):

    users = db.query(User).all()

    result = []

    for user in users:

        company = (
            db.query(UserCompany)
            .filter(
                UserCompany.user_id == user.id
            )
            .first()
        )

        result.append({
            "id": user.id,
            "username": user.username,
            "full_name": user.full_name,
            "role": user.role.name,
            "role_id": user.role_id,
            "company_name":
                company.company_name
                if company else None,
            "is_active": user.is_active
        })

    return result


# =========================
# Single User
# =========================

@router.get("/{user_id}")
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_administrator
    )
):

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:

        raise HTTPException(
            status_code=404,
            detail="کاربر یافت نشد"
        )

    company = (
        db.query(UserCompany)
        .filter(
            UserCompany.user_id == user.id
        )
        .first()
    )

    return {
        "id": user.id,
        "username": user.username,
        "full_name": user.full_name,
        "role_id": user.role_id,
        "company_name":
            company.company_name
            if company else None,
        "is_active": user.is_active
    }


# =========================
# Create User
# =========================

@router.post("")
def create_user(
    payload: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_administrator
    )
):

    existing_user = (
        db.query(User)
        .filter(
            User.username == payload.username
        )
        .first()
    )

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="نام کاربری تکراری است"
        )

    role = (
        db.query(Role)
        .filter(
            Role.id == payload.role_id
        )
        .first()
    )

    if not role:

        raise HTTPException(
            status_code=400,
            detail="نقش معتبر نیست"
        )

    if (
        role.name == "COMPANY_USER"
        and not payload.company_name
    ):

        raise HTTPException(
            status_code=400,
            detail="انتخاب شرکت الزامی است"
        )

    user = User(
        username=payload.username,
        hashed_password=get_password_hash(
            payload.password
        ),
        full_name=payload.full_name,
        role_id=payload.role_id,
        is_active=payload.is_active
    )

    db.add(user)

    db.flush()

    if role.name == "COMPANY_USER":

        db.add(
            UserCompany(
                user_id=user.id,
                company_name=payload.company_name
            )
        )

    db.commit()

    return {
        "message": "کاربر ایجاد شد"
    }


# =========================
# Update User
# =========================

@router.put("/{user_id}")
def update_user(
    user_id: int,
    payload: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_administrator
    )
):

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:

        raise HTTPException(
            status_code=404,
            detail="کاربر یافت نشد"
        )

    duplicate_user = (
        db.query(User)
        .filter(
            User.username == payload.username,
            User.id != user_id
        )
        .first()
    )

    if duplicate_user:

        raise HTTPException(
            status_code=400,
            detail="نام کاربری تکراری است"
        )

    role = (
        db.query(Role)
        .filter(
            Role.id == payload.role_id
        )
        .first()
    )

    if not role:

        raise HTTPException(
            status_code=400,
            detail="نقش معتبر نیست"
        )

    if (
        role.name == "COMPANY_USER"
        and not payload.company_name
    ):

        raise HTTPException(
            status_code=400,
            detail="انتخاب شرکت الزامی است"
        )

    user.username = payload.username
    user.full_name = payload.full_name
    user.role_id = payload.role_id
    user.is_active = payload.is_active

    if (
        payload.password
        and payload.password.strip()
    ):

        user.hashed_password = (
            get_password_hash(
                payload.password
            )
        )

    db.query(UserCompany).filter(
        UserCompany.user_id == user.id
    ).delete()

    if role.name == "COMPANY_USER":

        db.add(
            UserCompany(
                user_id=user.id,
                company_name=payload.company_name
            )
        )

    db.commit()

    return {
        "message": "کاربر بروزرسانی شد"
    }