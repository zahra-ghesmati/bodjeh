from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class BscIndicators(Base):
    __tablename__ = "BSC Indicators"
    __table_args__ = {"schema": "Report_Main"}
        # id به عنوان کلید اصلی (مطابق دیتابیس جدید)
    id = Column(Integer, primary_key=True, autoincrement=True)
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    mghdar_shakhs_vaghy_sal_jary = Column("مقدار شاخص - واقعی سال جاری", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    شاخص_bsc = Column("شاخص BSC", NVARCHAR(255))
    mghdar_shakhs_bvdjh = Column("مقدار شاخص - بودجه", NVARCHAR(255))
    mghdar_shakhs_bvdjh2 = Column("مقدار شاخص - بودجه2", NVARCHAR(255))
    mghdar_shakhs_bvdjh3 = Column("مقدار شاخص - بودجه3", NVARCHAR(255))
    mghdar_shakhs_dvrh_mshabh = Column("مقدار شاخص - دوره مشابه", NVARCHAR(255))
