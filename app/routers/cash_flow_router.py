from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional, List, Dict, Any

from app.database import get_db
from app.services.auth_service import get_current_user
from app.models.cash_flow import CashFlow
from app.services.access_service import check_access
from app.services.generic_form_service import check_form_permission

router = APIRouter(prefix="/forms/cash_flow", tags=["Cash Flow"])

SAROJ = "بين المللي ساروج بوشهر"

SAROJ_TEMPLATE = [
    "جمع موجودی اول دوره",
    "جمع وجوه دریافتی",
    "وجوه دریافتی از مشتریان داخلی",
    "وجوه دریافتی از صادرات",
    "سپرده بانکی",
    "جریان نقد خروجی ناشی از افتتاح سپرده",
    "حقوق و عوارض گمرکی",
    "گمرک",
    "سایر دریافت‌ها*",
    "جمع وجوه پرداختی",
    "حقوق و دستمزد پرسنل",
    "حقوق و دستمزد شرکت خدماتی",
    "حق‌الزحمه مشاورین",
    "بازخرید سنوات کارکنان",
    "خرید کالا و محصول",
    "خرید مواد اولیه",
    "پیش‌پرداخت‌ها",
    "ملزومات و قطعات مصرفی",
    "آب و برق و گاز و سوخت",
    "خرید دارایی ثابت",
    "هزینه اجاره محل",
    "سود پرداختی بابت تسهیلات مالی",
    "بازپرداخت تسهیلات",
    "سرمایه‌گذاری در صندوق‌های با درآمد ثابت",
    "سود سهام پرداختی",
    "سایر پرداخت‌ها*",
    "موجودی نقد نزد بانک",
    "مانده وجه نقد در پایان ماه",
]

OTHER_TEMPLATE = [
    "جمع موجودی اول دوره",
    "جمع وجوه دریافتی",
    "وجوه دریافتی از مشتریان",
    "سایر دریافت‌ها*",
    "جمع وجوه پرداختی",
    "حقوق و دستمزد پرسنل",
    "حقوق و دستمزد شرکت خدماتی",
    "حق الزحمه مشاورین",
    "بازخرید سنوات کارکنان",
    "خرید کالا و محصول",
    "خرید مواد اولیه",
    "پیش پرداخت ها",
    "ملزومات و قطعات مصرفی",
    "آب و برق و گاز و تلفن",
    "خرید دارایی ثابت",
    "هزینه اجاره محل",
    "سود پرداختی بابت تسهیلات مالی",
    "بازپرداخت تسهیلات",
    "جریان نقد خروجی ناشی از خرید اوراق بهادار",
    "سرمایه گذاری در صندوق های با درآمد ثابت",
    "سود سهام پرداختی",
    "سایر پرداخت‌ها*",
    "مانده وجه نقد در پایان ماه",
]

MONTH_FIELDS = [
    "dy", "bhmn", "asfnd", "frvrdyn", "ardybhsht",
    "khrdad", "tyr", "mrdad", "shhryvr", "mhr", "aban", "azr"
]

MONTH_LABELS = {
    "dy": "دی", "bhmn": "بهمن", "asfnd": "اسفند",
    "frvrdyn": "فروردین", "ardybhsht": "اردیبهشت", "khrdad": "خرداد",
    "tyr": "تیر", "mrdad": "مرداد", "shhryvr": "شهریور",
    "mhr": "مهر", "aban": "آبان", "azr": "آذر"
}

# ستون های جمع/مانده که واریدیشن روشون اعمال میشه
TOTAL_ROWS = {"جمع وجوه دریافتی", "جمع وجوه پرداختی"}
SAYR_ROWS_DARYAFTI = {"سایر دریافت‌ها*"}
SAYR_ROWS_PARDAKHTI = {"سایر پرداخت‌ها*"}


def row_to_dict(row: CashFlow):
    values = {
        "nvan": row.nvan,
        "shrh": row.shrh,
        "mjmv": row.mjmv,
    }
    for f in MONTH_FIELDS:
        values[f] = getattr(row, f)
    return {"id": row.id, "values": values}


def get_template(company: str):
    template = SAROJ_TEMPLATE if company == SAROJ else OTHER_TEMPLATE
    return [
        {"id": None, "values": {"nvan": t, "shrh": None, "mjmv": None,
                                 **{f: None for f in MONTH_FIELDS}}}
        for t in template
    ]


@router.get("/meta")
def get_meta():
    return {
        "title": "جریان وجوه نقد",
        "type": "cash_flow",
        "approval": {"type": "single"},
        "month_fields": MONTH_FIELDS,
        "month_labels": MONTH_LABELS,
    }


@router.get("/rows")
def get_rows(
    company: str,
    year: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    check_access(db, current_user, company)
    check_form_permission(db, "cash_flow", company)

    rows = (
        db.query(CashFlow)
        .filter(CashFlow.nam_shrkt == company, CashFlow.sal_maly == year)
        .all()
    )

    if not rows:
        return get_template(company)

    return [row_to_dict(r) for r in rows]


class CashFlowRowPayload(BaseModel):
    id: Optional[int] = None
    values: Dict[str, Any]


class SaveCashFlowRequest(BaseModel):
    company: str
    year: str
    rows: List[CashFlowRowPayload]


@router.post("/save")
def save_rows(
    payload: SaveCashFlowRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    check_access(db, current_user, payload.company)
    check_form_permission(db, "cash_flow", payload.company)

    try:
        # حذف همه ردیف های قبلی برای این شرکت+سال
        db.query(CashFlow).filter(
            CashFlow.nam_shrkt == payload.company,
            CashFlow.sal_maly == payload.year,
        ).delete()

        for row in payload.rows:
            v = row.values
            obj = CashFlow(
                nam_shrkt=payload.company,
                sal_maly=payload.year,
                nvan=v.get("nvan"),
                shrh=v.get("shrh"),
                mjmv=v.get("mjmv"),
            )
            for f in MONTH_FIELDS:
                val = v.get(f)
                setattr(obj, f, str(val) if val not in (None, "") else None)
            db.add(obj)

        db.commit()
        return {"status": "success"}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
