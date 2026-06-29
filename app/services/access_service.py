from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.user_models import User
from app.models.report_confirmation import PeriodLock # تغییر مسیر import

def check_access(db: Session, user: User, company: str):
    # ادمین‌ها به همه چیز دسترسی دارند
    if user.role.name in ["ADMINISTRATOR", "ADMIN"]:
        return True
    
    # برای کاربر عادی چک کن آیا شرکت در لیستش هست
    allowed_companies = [c.company_name for c in user.companies]
    if company not in allowed_companies:
        raise HTTPException(status_code=403, detail="شما دسترسی به این شرکت را ندارید.")
    return True

def is_period_locked(db: Session, form_key: str, company: str, year: str, month: str, type: str):
    lock = db.query(PeriodLock).filter(
        PeriodLock.form_key == form_key,
        PeriodLock.company == company,
        PeriodLock.sal_maly == year,
        PeriodLock.mah == month
    ).first()
    
    if not lock:
        return False
    
    if type == "budget" and lock.budget_approved:
        return True
    if type == "actual" and lock.actual_approved:
        return True
    return False
