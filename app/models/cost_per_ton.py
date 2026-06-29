from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)

from ..database import Base


class CostPerTon(Base):

    __tablename__ = "Cost per ton"
    __table_args__ = {
        "schema": "Report_Main"
    }

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    nam_shrkt = Column(
        "نام شرکت",
        NVARCHAR(255)
    )

    sal_maly = Column(
        "سال مالی",
        NVARCHAR(255)
    )

    mah_zarsh = Column(
        "ماه گزارش",
        NVARCHAR(255)
    )

    ajza_bhay_tmam_shdh_hr_tn = Column(
        "اجزاء بهای تمام شده هر تن",
        NVARCHAR(255)
    )

    bhay_tmam_shdh_hr_tn_bvdjh = Column(
        "بهای تمام شده هر تن - بودجه",
        Float
    )

    bhay_tmam_shdh_hr_tn_vaghy_sal_jary = Column(
        "بهای تمام شده هر تن - واقعی سال جاری",
        Float
    )

    bhay_tmam_shdh_hr_tn_bvdjh2 = Column(
        "بهای تمام شده هر تن - بودجه2",
        Float
    )

    bhay_tmam_shdh_hr_tn_bvdjh3 = Column(
        "بهای تمام شده هر تن - بودجه3",
        Float
    )

    bhay_tmam_shdh_hr_tn_dvrh_mshabh = Column(
        "بهای تمام شده هر تن - دوره مشابه",
        Float
    )