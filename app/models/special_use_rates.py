from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class SpecialUseRates(Base):
    __tablename__ = "Special use rates"
    __table_args__ = {"schema": "Report_Main"}

            # id به عنوان کلید اصلی (مطابق دیتابیس جدید)
    id = Column(Integer, primary_key=True, autoincrement=True)

    nrkh_msarf_vy_h_vaghy_sal_jary = Column("نرخ مصارف ویژه - واقعی سال جاری", Float )
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    msarf_vy_h = Column("مصارف ویژه", NVARCHAR(255))
    nv_klynkrsyman = Column("نوع کلینکر/سیمان", NVARCHAR(255))
    nrkh_msarf_vy_h_bvdjh = Column("نرخ مصارف ویژه - بودجه", Float )
    nrkh_msarf_vy_h_bvdjh2 = Column("نرخ مصارف ویژه - بودجه2", Float )
    nrkh_msarf_vy_h_bvdjh3 = Column("نرخ مصارف ویژه - بودجه3", Float )
    nrkh_msarf_vy_h_dvrh_mshabh = Column("نرخ مصارف ویژه - دوره مشابه", Float )
