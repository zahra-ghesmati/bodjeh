from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class HumanResource6(Base):
    __tablename__ = "Human Resource 6"
    __table_args__ = {"schema": "Report_Main"}

            # id به عنوان کلید اصلی (مطابق دیتابیس جدید)
    id = Column(Integer, primary_key=True, autoincrement=True)

    tdad_prsnl_bh_tfkyk_thsylat_vaghy_sal_jary = Column("تعداد پرسنل به تفکیک تحصیلات - واقعی سال جاری", Float)
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    myzan_thsylat = Column("میزان تحصیلات", NVARCHAR(255))
    tdad_prsnl_bh_tfkyk_thsylat_bvdjh = Column("تعداد پرسنل به تفکیک تحصیلات - بودجه", Float)
    tdad_prsnl_bh_tfkyk_thsylat_bvdjh2 = Column("تعداد پرسنل به تفکیک تحصیلات - بودجه2", Float)
    tdad_prsnl_bh_tfkyk_thsylat_bvdjh3 = Column("تعداد پرسنل به تفکیک تحصیلات - بودجه3", Float)
    tdad_prsnl_bh_tfkyk_thsylat_dvrh_mshabh = Column("تعداد پرسنل به تفکیک تحصیلات - دوره مشابه",Float)
