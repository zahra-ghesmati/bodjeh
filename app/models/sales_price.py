from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class SalesPrice(Base):
    __tablename__ = "Sales Price"
    __table_args__ = {"schema": "Report_Main"}

            # id به عنوان کلید اصلی (مطابق دیتابیس جدید)
    id = Column(Integer, primary_key=True, autoincrement=True)

    nrkh_frvsh_vaghy_sal_jary = Column("نرخ فروش - واقعی سال جاری", Float )
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    nam_mhsvl_frvsh = Column("نام محصول فروش", NVARCHAR(255))
    nv_frvsh = Column("نوع فروش", NVARCHAR(255))
    nrkh_frvsh_bvdjh = Column("نرخ فروش - بودجه", Float )
    nrkh_frvsh_bvdjh2 = Column("نرخ فروش - بودجه2", Float )
    nrkh_frvsh_bvdjh3 = Column("نرخ فروش - بودجه3", Float )
    nrkh_frvsh_dvrh_mshabh = Column("نرخ فروش - دوره مشابه", Float )
