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

year = "1404-1405"

all_months = [
    "دي",
    "بهمن",
    "اسفند",
    "فروردين",
    "ارديبهشت",
    "خرداد",
    "تير",
    "مرداد",
    "شهريور",
    "مهر",
    "آبان",
    "آذر"
]

actual_months = [
    "دي",
    "بهمن",
    "اسفند"
]

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

            # تایید بودجه همه ماه‌ها
            lock.budget_approved = True
            lock.budget_approved_at = datetime.now()

            # تایید عملکرد فقط دی، بهمن، اسفند
            if month in actual_months:

                lock.actual_approved = True
                lock.actual_approved_at = datetime.now()

            else:

                lock.actual_approved = False
                lock.actual_approved_at = None

db.commit()

print("DONE")