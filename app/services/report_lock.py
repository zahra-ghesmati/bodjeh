from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.report_confirmation import ReportConfirmation


def check_report_locked(db: Session, table_name, company, year, month):

    status = db.query(ReportConfirmation).filter(
        ReportConfirmation.table_name == table_name,
        ReportConfirmation.company_name == company,
        ReportConfirmation.fiscal_year == year,
        ReportConfirmation.report_month == month,
        ReportConfirmation.is_confirmed == True
    ).first()

    if status:
        raise HTTPException(
            status_code=403,
            detail="این گزارش قبلاً تایید شده و قابل ویرایش نیست"
        )
