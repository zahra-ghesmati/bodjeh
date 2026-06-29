from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class Production(Base):
    __tablename__ = "Production"
    __table_args__ = {"schema": "Report_Main"}

            # id به عنوان کلید اصلی (مطابق دیتابیس جدید)
    id = Column(Integer, primary_key=True, autoincrement=True)

    myzan_tvlyd_vaghy_sal_jary = Column("میزان تولید - واقعی سال جاری", Float )
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    nam_mhsvl_tvlydy = Column("نام محصول تولیدی", NVARCHAR(255))
    myzan_tvlyd_bvdjh = Column("میزان تولید - بودجه", Float )
    myzan_tvlyd_bvdjh2 = Column("میزان تولید - بودجه2", Float )
    myzan_tvlyd_bvdjh3 = Column("میزان تولید - بودجه3", Float )
    myzan_tvlyd_dvrh_mshabh = Column("میزان تولید - دوره مشابه", Float )
