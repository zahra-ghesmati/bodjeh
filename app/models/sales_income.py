from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class SalesIncome(Base):
    __tablename__ = "Sales income"
    __table_args__ = {"schema": "Report_Main"}

            # id به عنوان کلید اصلی (مطابق دیتابیس جدید)
    id = Column(Integer, primary_key=True, autoincrement=True)

    frvsh_khals_ryaly_vaghy_sal_jary = Column("فروش خالص ریالی - واقعی سال جاری", Float )
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    nam_mhsvl_frvsh = Column("نام محصول فروش", NVARCHAR(255))
    nv_frvsh = Column("نوع فروش", NVARCHAR(255))
    frvsh_khals_ryaly_bvdjh = Column("فروش خالص ریالی - بودجه", Float )
    frvsh_khals_ryaly_bvdjh2 = Column("فروش خالص ریالی - بودجه2", Float )
    frvsh_khals_ryaly_bvdjh3 = Column("فروش خالص ریالی - بودجه3", Float )
    frvsh_khals_ryaly_dvrh_mshabh = Column("فروش خالص ریالی - دوره مشابه", Float )
