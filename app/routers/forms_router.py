import logging

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from ..database import get_db
from app.services.auth_service import get_current_user
from app.services.form_dispatcher import (
    get_rows_generic,
    save_rows_generic,
    get_form_meta,
    get_forms_menu
)
from app.schemas.base_form import SaveFormRequest

router = APIRouter(prefix="/forms", tags=["Forms"])

@router.get("/menu")
def get_menu(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return get_forms_menu(
        db=db,
        current_user=current_user
    )
# =========================



# =========================
# Rows (GENERIC)
# =========================
@router.get("/{form_key}/rows", dependencies=[Depends(get_current_user)])
def get_rows(
    form_key: str,
    company: str,
    year: str,
    month: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return get_rows_generic(
        form_key=form_key,
        db=db,
        company=company,
        year=year,
        month=month,
        current_user=current_user
    )


# =========================
# Save (GENERIC)
# =========================
@router.post("/{form_key}/save", dependencies=[Depends(get_current_user)])
def save_rows(
    form_key: str,
    payload: SaveFormRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return save_rows_generic(
        form_key=form_key,
        db=db,
        payload=payload,
        current_user=current_user
    )


@router.get("/{form_key}/meta")
def get_meta(form_key: str):
    return get_form_meta(form_key)

