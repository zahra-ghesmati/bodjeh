from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class Revenues(Base):
    __tablename__ = "Revenues"
    __table_args__ = {"schema": "Report_Main"}

            # id به عنوان کلید اصلی (مطابق دیتابیس جدید)
    id = Column(Integer, primary_key=True, autoincrement=True)

    dramd_khals_vaghy_sal_jary = Column("درآمد خالص - واقعی سال جاری", NVARCHAR(255) )
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    dramd = Column("درآمد", NVARCHAR(255))
    nv_dramd = Column("نوع درآمد", NVARCHAR(255))
    dramd_khals_bvdjh = Column("درآمد خالص - بودجه", NVARCHAR(255) )
    dramd_khals_bvdjh2 = Column("درآمد خالص - بودجه2", NVARCHAR(255) )
    dramd_khals_bvdjh3 = Column("درآمد خالص - بودجه3", NVARCHAR(255) )
    dramd_khals_dvrh_mshabh = Column("درآمد خالص - دوره مشابه", NVARCHAR(255) )
