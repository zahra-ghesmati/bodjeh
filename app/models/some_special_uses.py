from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class SomeSpecialUses(Base):
    __tablename__ = "Some special uses"
    __table_args__ = {"schema": "Report_Main"}
            # id به عنوان کلید اصلی (مطابق دیتابیس جدید)
    id = Column(Integer, primary_key=True, autoincrement=True)
    mghdar_msarf_vy_h_vaghy_sal_jary = Column("مقدار مصارف ویژه - واقعی سال جاری", Float)
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    msarf_vy_h = Column("مصارف ویژه", NVARCHAR(255))
    nv_klynkrsyman = Column("نوع کلینکر/سیمان", NVARCHAR(255))
    mghdar_msarf_vy_h_bvdjh = Column("مقدار مصارف ویژه - بودجه", Float)
    mghdar_msarf_vy_h_bvdjh2 = Column("مقدار مصارف ویژه - بودجه2",Float)
    mghdar_msarf_vy_h_bvdjh3 = Column("مقدار مصارف ویژه - بودجه3",Float)
    mghdar_msarf_vy_h_dvrh_mshabh = Column("مقدار مصارف ویژه - دوره مشابه", Float)
