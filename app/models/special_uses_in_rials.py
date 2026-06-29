from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class SpecialUsesInRials(Base):
    __tablename__ = "Special uses in Rials"
    __table_args__ = {"schema": "Report_Main"}

            # id به عنوان کلید اصلی (مطابق دیتابیس جدید)
    id = Column(Integer, primary_key=True, autoincrement=True)

    mblgh_msarf_vy_h_vaghy_sal_jary = Column("مبلغ مصارف ویژه- واقعی سال جاری", NVARCHAR(255) )
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    msarf_vy_h = Column("مصارف ویژه", NVARCHAR(255))
    nv_klynkrsyman = Column("نوع کلینکر/سیمان", NVARCHAR(255))
    mblgh_msarf_vy_h_bvdjh = Column("مبلغ مصارف ویژه- بودجه", Float )
    mblgh_msarf_vy_h_bvdjh2 = Column("مبلغ مصارف ویژه- بودجه2", Float )
    mblgh_msarf_vy_h_bvdjh3 = Column("مبلغ مصارف ویژه- بودجه3", Float )
    mblgh_msarf_vy_h_dvrh_mshabh = Column("مبلغ مصارف ویژه - دوره مشابه", Float )
