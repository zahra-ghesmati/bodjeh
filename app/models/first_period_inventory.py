from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class FirstPeriodInventory(Base):
    __tablename__ = "First period inventory"
    __table_args__ = {"schema": "Report_Main"}
        # id به عنوان کلید اصلی (مطابق دیتابیس جدید)
    id = Column(Integer, primary_key=True, autoincrement=True)
    mvjvdy_abtday_dvrh_vaghy_sal_jary = Column("موجودی ابتدای دوره - واقعی سال جاری", Float)
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    nam_mhsvl_tvlydy = Column("نام محصول تولیدی", NVARCHAR(255))
    mvjvdy_abtday_dvrh_bvdjh = Column("موجودی ابتدای دوره - بودجه", Float)
    mvjvdy_abtday_dvrh_bvdjh2 = Column("موجودی ابتدای دوره - بودجه2",Float)
    mvjvdy_abtday_dvrh_bvdjh3 = Column("موجودی ابتدای دوره - بودجه3",Float)
    mvjvdy_abtday_dvrh_dvrh_mshabh = Column("موجودی ابتدای دوره - دوره مشابه",Float)
