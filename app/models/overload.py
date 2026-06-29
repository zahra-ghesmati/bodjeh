from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class Overload(Base):
    __tablename__ = "Overload"
    __table_args__ = {"schema": "Report_Main"}

            # id به عنوان کلید اصلی (مطابق دیتابیس جدید)
    id = Column(Integer, primary_key=True, autoincrement=True)

    hzynh_srbar_vaghy_sal_jary = Column("هزینه سربار - واقعی سال جاری", Float)
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    nvan_hzynh_srbar = Column("عنوان هزینه سربار", NVARCHAR(255))
    hzynh_srbar_bvdjh = Column("هزینه سربار - بودجه", Float)
    hzynh_srbar_bvdjh2 = Column("هزینه سربار - بودجه2", Float)
    hzynh_srbar_bvdjh3 = Column("هزینه سربار - بودجه3", Float)
    hzynh_srbar_dvrh_mshabh = Column("هزینه سربار - دوره مشابه", Float)
