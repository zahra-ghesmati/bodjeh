from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class CashAndCreditSales(Base):
    __tablename__ = "Cash and credit sales"
    __table_args__ = {"schema": "Report_Main"}
        # id به عنوان کلید اصلی (مطابق دیتابیس جدید)
    id = Column(Integer, primary_key=True, autoincrement=True)
    frvsh_khals_vaghy_sal_jary = Column("فروش خالص - واقعی سال جاری", Float)
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    nv_frvsh = Column("نوع فروش", NVARCHAR(255))
    frvsh_khals_bvdjh = Column("فروش خالص - بودجه", Float)
    frvsh_khals_bvdjh2 = Column("فروش خالص - بودجه2",Float)
    frvsh_khals_bvdjh3 = Column("فروش خالص - بودجه3", Float)
    frvsh_khals_dvrh_mshabh = Column("فروش خالص - دوره مشابه", Float)
