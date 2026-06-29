from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.database import get_db
from app.models.month import Month
from app.models.user_models import User
from app.services.auth_service import get_current_user

from datetime import datetime
router = APIRouter(
    prefix="/api/months",
    tags=["Months"]
)


# =========================
# Month Seed (Refactored)
# =========================
def get_month_seed():
    return [
        ("دي", "01", "سه ماهه اول"),
        ("بهمن", "02", "سه ماهه اول"),
        ("اسفند", "03", "سه ماهه اول"),

        ("فروردين", "04", "سه ماهه دوم"),
        ("ارديبهشت", "05", "سه ماهه دوم"),
        ("خرداد", "06", "سه ماهه دوم"),

        ("تير", "07", "سه ماهه سوم"),
        ("مرداد", "08", "سه ماهه سوم"),
        ("شهريور", "09", "سه ماهه سوم"),

        ("مهر", "10", "سه ماهه چهارم"),
        ("آبان", "11", "سه ماهه چهارم"),
        ("آذر", "12", "سه ماهه چهارم")
    ]


# =========================
# Auth Guard
# =========================
def require_administrator(
    current_user: User = Depends(get_current_user)
):
    if current_user.role.name != "ADMINISTRATOR":
        raise HTTPException(
            status_code=403,
            detail="دسترسی غیرمجاز"
        )
    return current_user


# =========================
# Years List
# =========================
@router.get("/years")
def get_years(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    years = (
        db.query(Month.sal)
        .distinct()
        .order_by(Month.sal.desc())
        .all()
    )

    return [y[0] for y in years if y[0]]

#=============

@router.get("/current-period")
def get_current_period(
    db: Session = Depends(get_db)
):
    print(datetime.now())
    latest_year = (
        db.query(Month.sal)
        .distinct()
        .order_by(Month.sal.desc())
        .first()
    )

    if not latest_year:

        raise HTTPException(
            status_code=404,
            detail="سال مالی یافت نشد"
        )

    months = (
        db.query(Month)
        .filter(
            Month.sal == latest_year[0]
        )
        .order_by(
            Month.shmarh_mah
        )
        .all()
    )

    current_month = datetime.now().month

    month_map = {
        1: "دي",
        2: "بهمن",
        3: "اسفند",
        4: "فروردين",
        5: "ارديبهشت",
        6: "خرداد",
        7: "تير",
        8: "مرداد",
        9: "شهريور",
        10: "مهر",
        11: "آبان",
        12: "آذر"
    }

    current_persian_month = month_map.get(
        current_month
    )

    current_index = next(
        (
            i
            for i, m in enumerate(months)
            if m.mah_zarsh ==
            current_persian_month
        ),
        0
    )

    previous_index = (
        current_index - 1
    ) % len(months)

    return {
        "year": latest_year[0],
        "month":
            months[
                previous_index
            ].mah_zarsh
    } 
# =========================
# Year Details
# =========================
@router.get("/{year}")
def get_year(
    year: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_administrator)
):

    if not year:
        raise HTTPException(status_code=400, detail="سال نامعتبر است")

    rows = (
        db.query(Month)
        .filter(Month.sal == year)
        .order_by(Month.shmarh_mah)
        .all()
    )

    return [
        {
            "month": row.mah_zarsh,
            "month_number": row.shmarh_mah,
            "period": row.dvrh,
            "year": row.sal,
            "unic_code": row.unic_code,
            "month_number_2": row.shmarh_mah_2
        }
        for row in rows
    ]


# =========================
# Create Year
# =========================
@router.post("/{year}")
def create_year(
    year: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_administrator)
):

    exists = (
        db.query(Month)
        .filter(Month.sal == year)
        .first()
    )

    if exists:
        raise HTTPException(
            status_code=400,
            detail="این سال قبلا ثبت شده است"
        )

    try:
        seed = get_month_seed()

        rows = [
            Month(
                mah_zarsh=m[0],
                shmarh_mah=m[1],
                dvrh=m[2],
                sal=year,
                unic_code=f"{year}_{m[0]}",
                shmarh_mah_2=f"{year}{m[1].zfill(3)}"
            )
            for m in seed
        ]

        db.bulk_save_objects(rows)
        db.commit()

        return {
            "message": "سال مالی ایجاد شد"
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# =========================
# Delete Year
# =========================
@router.delete("/{year}")
def delete_year(
    year: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_administrator)
):

    rows = (
        db.query(Month)
        .filter(Month.sal == year)
        .all()
    )

    if not rows:
        raise HTTPException(
            status_code=404,
            detail="سال یافت نشد"
        )

    TABLES_WITH_YEAR = [
        {
            "name": "Admin costs",
            "table": "Admin costs",
            "schema": "Report_Main"
        }
    ]

    for t in TABLES_WITH_YEAR:

        query = text(f"""
            SELECT TOP 1 1
            FROM {t["schema"]}.[{t["table"]}]
            WHERE [سال مالی] = :year
        """)

        result = db.execute(query, {"year": year}).first()

        if result:
            raise HTTPException(
                status_code=400,
                detail=f"سال {year} در جدول {t['name']} دارای اطلاعات است و قابل حذف نیست."
            )

    try:

        (
            db.query(Month)
            .filter(Month.sal == year)
            .delete()
        )

        db.commit()

        return {
            "message": "سال حذف شد"
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    

