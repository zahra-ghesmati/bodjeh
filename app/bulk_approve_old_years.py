from datetime import datetime

from app.models import user_models
from app.models.user_models import User

from app.database import SessionLocal
from app.models.report_confirmation import PeriodLock
from app.config.form_configs import SERVICE_MAP

db = SessionLocal()

companies = [
    "سيمان مازندران",
    "گروه صنايع سيمان کرمان",
    "بين المللي ساروج بوشهر",
    "سيمان شمال",
    "توليدي سيمان فيروزکوه"
]

years = [
    "1399-1400",
    "1400-1401",
    "1401-1402",
    "1402-1403",
    "1403-1404"
]

all_months = [
    "فروردين",
    "ارديبهشت",
    "خرداد",
    "تير",
    "مرداد",
    "شهريور",
    "مهر",
    "آبان",
    "آذر",
    "دي",
    "بهمن",
    "اسفند"
]

for year in years:

    for company in companies:

        for month in all_months:

            for form_key in SERVICE_MAP.keys():

                lock = (
                    db.query(PeriodLock)
                    .filter(
                        PeriodLock.form_key == form_key,
                        PeriodLock.company == company,
                        PeriodLock.sal_maly == year,
                        PeriodLock.mah == month
                    )
                    .first()
                )

                if not lock:

                    lock = PeriodLock(
                        form_key=form_key,
                        company=company,
                        sal_maly=year,
                        mah=month
                    )

                    db.add(lock)

                lock.budget_approved = True
                lock.budget_approved_at = datetime.now()

                lock.actual_approved = True
                lock.actual_approved_at = datetime.now()

db.commit()

print("OLD YEARS APPROVED")