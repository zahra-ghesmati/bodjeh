from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class HumanResource5(Base):
    __tablename__ = "Human Resource 5"
    __table_args__ = {"schema": "Report_Main"}

            # id به عنوان کلید اصلی (مطابق دیتابیس جدید)
    id = Column(Integer, primary_key=True, autoincrement=True)

    tdad_prsnl_bh_tfkyk_sn_vaghy_sal_jary = Column("تعداد پرسنل به تفکیک سن - واقعی سال جاری",Float)
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    tfkyk_sn = Column("تفکیک سن", NVARCHAR(255))
    tdad_prsnl_bh_tfkyk_sn_bvdjh = Column("تعداد پرسنل به تفکیک سن - بودجه", Float)
    tdad_prsnl_bh_tfkyk_sn_bvdjh2 = Column("تعداد پرسنل به تفکیک سن - بودجه2", Float)
    tdad_prsnl_bh_tfkyk_sn_bvdjh3 = Column("تعداد پرسنل به تفکیک سن - بودجه3", Float)
    tdad_prsnl_bh_tfkyk_sn_dvrh_mshabh = Column("تعداد پرسنل به تفکیک سن - دوره مشابه", Float)
