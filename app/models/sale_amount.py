from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class SaleAmount(Base):
    __tablename__ = "Sale Amount"
    __table_args__ = {"schema": "Report_Main"}

            # id به عنوان کلید اصلی (مطابق دیتابیس جدید)
    id = Column(Integer, primary_key=True, autoincrement=True)

    frvsh_mghdary_vaghy_sal_jary = Column("فروش مقداری - واقعی سال جاری", Float )
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    nam_mhsvl_frvsh = Column("نام محصول فروش", NVARCHAR(255))
    nv_frvsh = Column("نوع فروش", NVARCHAR(255))
    frvsh_mghdary_bvdjh = Column("فروش مقداری - بودجه", Float )
    frvsh_mghdary_bvdjh2 = Column("فروش مقداری - بودجه2", Float )
    frvsh_mghdary_bvdjh3 = Column("فروش مقداری - بودجه3", Float )
    frvsh_mghdary_dvrh_mshabh = Column("فروش مقداری - دوره مشابه", Float )
