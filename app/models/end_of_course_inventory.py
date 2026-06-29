from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class EndOfCourseInventory(Base):
    __tablename__ = "End of course inventory"
    __table_args__ = {"schema": "Report_Main"}
        # id به عنوان کلید اصلی (مطابق دیتابیس جدید)
    id = Column(Integer, primary_key=True, autoincrement=True)
    mvjvdy_payan_dvrh_vaghy_sal_jary = Column("موجودی پایان دوره - واقعی سال جاری", Float)
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    nam_mhsvl_tvlydy = Column("نام محصول تولیدی", NVARCHAR(255))
    mvjvdy_payan_dvrh_bvdjh = Column("موجودی پایان دوره - بودجه", Float)
    mvjvdy_payan_dvrh_bvdjh2 = Column("موجودی پایان دوره - بودجه2",Float)
    mvjvdy_payan_dvrh_bvdjh3 = Column("موجودی پایان دوره - بودجه3", Float)
    mvjvdy_payan_dvrh_dvrh_mshabh = Column("موجودی پایان دوره - دوره مشابه", Float)
