from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class Stops(Base):
    __tablename__ = "Stops"
    __table_args__ = {"schema": "Report_Main"}
        # id به عنوان کلید اصلی (مطابق دیتابیس جدید)
    id = Column(Integer, primary_key=True, autoincrement=True)
    myzan_sat_tvghf_vaghy_sal_jary = Column("میزان ساعت توقف - واقعی سال جاری", NVARCHAR(255) )
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    kvrh = Column("کوره", NVARCHAR(255))
    myzan_sat_tvghf_bvdjh = Column("میزان ساعت توقف - بودجه", NVARCHAR(255) )
    myzan_sat_tvghf_bvdjh2 = Column("میزان ساعت توقف - بودجه2", NVARCHAR(255) )
    myzan_sat_tvghf_bvdjh3 = Column("میزان ساعت توقف - بودجه3", NVARCHAR(255) )
    myzan_sat_tvghf_dvrh_mshabh = Column("میزان ساعت توقف - دوره مشابه", NVARCHAR(255) )
