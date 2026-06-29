from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class HumanResource3(Base):
    __tablename__ = "Human Resource 3"
    __table_args__ = {"schema": "Report_Main"}
            # id به عنوان کلید اصلی (مطابق دیتابیس جدید)
    id = Column(Integer, primary_key=True, autoincrement=True)

    tdad_prsnl_bh_tfkyk_jnsyt_vaghy_sal_jary = Column("تعداد پرسنل به تفکیک جنسیت - واقعی سال جاری",Float)
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    jnsyt = Column("جنسیت", NVARCHAR(255))
    tdad_prsnl_bh_tfkyk_jnsyt_bvdjh = Column("تعداد پرسنل به تفکیک جنسیت - بودجه", Float )
    tdad_prsnl_bh_tfkyk_jnsyt_bvdjh2 = Column("تعداد پرسنل به تفکیک جنسیت - بودجه2", Float)
    tdad_prsnl_bh_tfkyk_jnsyt_bvdjh3 = Column("تعداد پرسنل به تفکیک جنسیت - بودجه3", Float)
    tdad_prsnl_bh_tfkyk_jnsyt_dvrh_mshabh = Column("تعداد پرسنل به تفکیک جنسیت - دوره مشابه", Float)
