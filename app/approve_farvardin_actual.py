from datetime import datetime
from app.models.report_confirmation import PeriodLock
from app.database import SessionLocal
from app.models.report_confirmation import PeriodLock
from app.config.form_configs import SERVICE_MAP
from app.database import SessionLocal

from app.models.user_models import User
from app.models.report_confirmation import PeriodLock
db = SessionLocal()

companies = [
    "سيمان مازندران",
    "گروه صنايع سيمان کرمان",
    "بين المللي ساروج بوشهر",
    "سيمان شمال",
    "توليدي سيمان فيروزکوه"
]

for company in companies:

    for form_key in SERVICE_MAP.keys():

        lock = (
            db.query(PeriodLock)
            .filter(
                PeriodLock.form_key == form_key,
                PeriodLock.company == company,
                PeriodLock.sal_maly == "1404-1405",
                PeriodLock.mah == "فروردين"
            )
            .first()
        )

        if not lock:

            lock = PeriodLock(
                form_key=form_key,
                company=company,
                sal_maly="1404-1405",
                mah="فروردين"
            )

            db.add(lock)

        lock.actual_approved = True
        lock.actual_approved_at = datetime.now()

db.commit()

print("DONE")