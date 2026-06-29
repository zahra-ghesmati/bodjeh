from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.report_confirmation import PeriodLock
from app.models.user_models import User
from app.services.auth_service import get_current_user
from app.config.form_configs import SERVICE_MAP as GENERIC_SERVICE_MAP
from app.config.dynamic_form_configs import SERVICE_MAP as DYNAMIC_SERVICE_MAP

SERVICE_MAP = {**GENERIC_SERVICE_MAP, **DYNAMIC_SERVICE_MAP}


router = APIRouter(prefix="/approvals", tags=["Approvals"])


class ApprovalRequest(BaseModel):
    form_key: str
    company: str
    year: str
    month: str



def get_or_create_lock(
    db: Session,
    form_key: str,
    company: str,
    year: str,
    month: str
):

    lock = db.query(PeriodLock).filter(
        PeriodLock.form_key == form_key,
        PeriodLock.company == company,
        PeriodLock.sal_maly == year,
        PeriodLock.mah == month
    ).first()


    if not lock:

        lock = PeriodLock(
            form_key=form_key,
            company=company,
            sal_maly=year,
            mah=month
        )

        db.add(lock)
        db.flush()


    return lock



def validate_before_approval(
    db,
    form_key,
    company,
    year,
    month,
    mode
):

    config = SERVICE_MAP.get(form_key)


    if not config:
        raise HTTPException(
            status_code=404,
            detail="فرم یافت نشد"
        )

    # --- اضافه کن از اینجا ---
    if form_key == "cash_flow":
        from app.models.cash_flow import CashFlow
        rows = db.query(CashFlow).filter(
            CashFlow.nam_shrkt == company,
            CashFlow.sal_maly == year,
        ).all()
        if not rows:
            raise HTTPException(status_code=400, detail="هیچ داده‌ای برای تایید وجود ندارد.")
        return  # validation تموم شد، ادامه نده

    Model = config["model"]


    rows = db.query(Model).filter(
        Model.nam_shrkt == company,
        Model.sal_maly == year,
        Model.mah_zarsh == month
    ).all()


    if not rows:
        raise HTTPException(
            status_code=400,
            detail="هیچ داده‌ای برای تایید وجود ندارد."
        )


    #
    # Dynamic forms
    #
    if config.get("type") == "dynamic":


        approval = config.get(
            "approval",
            {
                "type":"single"
            }
        )


        if approval.get("type") == "double":


            if mode == "budget":

                fields = approval.get(
                    "budget_fields",
                    []
                )

            else:

                fields = approval.get(
                    "actual_fields",
                    []
                )


        else:

            fields = [
                col["field"]
                for col in config.get(
                    "columns",
                    []
                )
            ]



        for row in rows:

            for field in fields:

                value = getattr(
                    row,
                    field,
                    None
                )


                if value is None:

                    raise HTTPException(
                        status_code=400,
                        detail="اطلاعات فرم کامل نشده است."
                    )


        return



    #
    # Generic forms
    #
    field_name = (
        config["budget_field"]
        if mode == "budget"
        else config["actual_field"]
    )


    has_null = any(
        getattr(row, field_name) is None
        for row in rows
    )


    if has_null:

        raise HTTPException(
            status_code=400,
            detail="اطلاعات فرم کامل نشده است."
        )





@router.get("/status")
def get_status(
    form_key: str,
    company: str,
    year: str,
    month: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    lock = db.query(PeriodLock).filter(
        PeriodLock.form_key == form_key,
        PeriodLock.company == company,
        PeriodLock.sal_maly == year,
        PeriodLock.mah == month
    ).first()


    if not lock:

        return {
            "approval_type":
                SERVICE_MAP.get(form_key, {})
                .get("approval", {})
                .get("type","single"),

            "budget_approved":False,
            "actual_approved":False
        }



    return {

        "approval_type":
            SERVICE_MAP.get(form_key, {})
            .get("approval", {})
            .get("type","single"),

        "budget_approved": lock.budget_approved,

        "actual_approved": lock.actual_approved
    }





@router.post("/budget")
def approve_budget(
    payload: ApprovalRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    if current_user.role.name not in [
        "ADMIN",
        "ADMINISTRATOR"
    ]:
        raise HTTPException(403)



    validate_before_approval(
        db=db,
        form_key=payload.form_key,
        company=payload.company,
        year=payload.year,
        month=payload.month,
        mode="budget"
    )



    lock = get_or_create_lock(
        db,
        payload.form_key,
        payload.company,
        payload.year,
        payload.month
    )



    lock.budget_approved=True
    lock.budget_approved_at=datetime.now()
    lock.budget_approved_by=current_user.id


    db.commit()


    return {
        "success":True
    }





@router.delete("/budget")
def unapprove_budget(
    payload: ApprovalRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    if current_user.role.name != "ADMINISTRATOR":
        raise HTTPException(403)



    lock=get_or_create_lock(
        db,
        payload.form_key,
        payload.company,
        payload.year,
        payload.month
    )


    lock.budget_approved=False
    lock.budget_approved_at=None
    lock.budget_approved_by=None


    db.commit()


    return {
        "success":True
    }





@router.post("/actual")
def approve_actual(
    payload: ApprovalRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    if current_user.role.name not in [
        "ADMIN",
        "ADMINISTRATOR"
    ]:
        raise HTTPException(403)



    validate_before_approval(
        db=db,
        form_key=payload.form_key,
        company=payload.company,
        year=payload.year,
        month=payload.month,
        mode="actual"
    )



    lock=get_or_create_lock(
        db,
        payload.form_key,
        payload.company,
        payload.year,
        payload.month
    )


    lock.actual_approved=True
    lock.actual_approved_at=datetime.now()
    lock.actual_approved_by=current_user.id


    db.commit()


    return {
        "success":True
    }





@router.delete("/actual")
def unapprove_actual(
    payload: ApprovalRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    if current_user.role.name != "ADMINISTRATOR":
        raise HTTPException(403)



    lock=get_or_create_lock(
        db,
        payload.form_key,
        payload.company,
        payload.year,
        payload.month
    )


    lock.actual_approved=False
    lock.actual_approved_at=None
    lock.actual_approved_by=None


    db.commit()


    return {
        "success":True
    }