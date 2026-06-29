from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class RawMaterialConsumptionPrice(Base):
    __tablename__ = "Raw Material Consumption Price"
    __table_args__ = {"schema": "Report_Main"}

            # id به عنوان کلید اصلی (مطابق دیتابیس جدید)
    id = Column(Integer, primary_key=True, autoincrement=True)

    nrkh_msrf_mvad_avlyh_vaghy_sal_jary = Column("نرخ مصرف مواد اولیه - واقعی سال جاری", Float )
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    mvad_avlyh = Column("مواد اولیه", NVARCHAR(255))
    nv_klynkrsyman = Column("نوع کلینکر/سیمان", NVARCHAR(255))
    nrkh_msrf_mvad_avlyh_bvdjh = Column("نرخ مصرف مواد اولیه - بودجه", Float )
    nrkh_msrf_mvad_avlyh_bvdjh2 = Column("نرخ مصرف مواد اولیه - بودجه2", Float )
    nrkh_msrf_mvad_avlyh_bvdjh3 = Column("نرخ مصرف مواد اولیه - بودجه3", Float )
    nrkh_msrf_mvad_avlyh_dvrh_mshabh = Column("نرخ مصرف مواد اولیه - دوره مشابه", Float )
