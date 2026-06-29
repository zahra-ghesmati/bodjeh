from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.auth_service import get_current_user
from app.services.dashboard_service import (
    get_dashboard_status
)
from app.services.dashboard_service import (
    get_dashboard_status,
    get_admin_dashboard_status
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/status")
def dashboard_status(
    company: str,
    year: str,
    month: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return get_dashboard_status(
        db=db,
        company=company,
        year=year,
        month=month,
        current_user=current_user
    )



@router.get("/admin")
def admin_dashboard(
    year: str,
    month: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return get_admin_dashboard_status(
        db=db,
        year=year,
        month=month,
        current_user=current_user
    )