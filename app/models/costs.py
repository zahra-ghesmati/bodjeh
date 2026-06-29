from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class Costs(Base):
    __tablename__ = "Costs"
    __table_args__ = {"schema": "Report_Main"}
        # id به عنوان کلید اصلی (مطابق دیتابیس جدید)
    id = Column(Integer, primary_key=True, autoincrement=True)
    mblgh_vaghy_sal_jary = Column("مبلغ - واقعی سال جاری", NVARCHAR(255))
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    ajza_bhay_tmam_shdh_jam = Column("اجزاء بهای تمام شده جامع", NVARCHAR(255))
    mblgh_bvdjh = Column("مبلغ - بودجه", NVARCHAR(255) )
    mblgh_bvdjh2 = Column("مبلغ - بودجه2", NVARCHAR(255) )
    mblgh_bvdjh3 = Column("مبلغ - بودجه3", NVARCHAR(255) )
    mblgh_dvrh_mshabh = Column("مبلغ - دوره مشابه", NVARCHAR(255) )
