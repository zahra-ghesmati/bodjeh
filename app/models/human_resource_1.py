from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class HumanResource1(Base):
    __tablename__ = "Human Resource 1"
    __table_args__ = {"schema": "Report_Main"}
            # id به عنوان کلید اصلی (مطابق دیتابیس جدید)
    id = Column(Integer, primary_key=True, autoincrement=True)
    tdad_prsnl_bh_tfkyk_nv_ghrardad_vaghy_sal_jary = Column("تعداد پرسنل به تفکیک نوع قرارداد - واقعی سال جاری", Float)
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    nam_shrkt_1 = Column("نام شرکت (#1)", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    nv_ghrardad = Column("نوع قرارداد", NVARCHAR(255))
    tdad_prsnl_bh_tfkyk_nv_ghrardad_bvdjh = Column("تعداد پرسنل به تفکیک نوع قرارداد - بودجه", Float)
    tdad_prsnl_bh_tfkyk_nv_ghrardad_bvdjh2 = Column("تعداد پرسنل به تفکیک نوع قرارداد - بودجه2", Float)
    tdad_prsnl_bh_tfkyk_nv_ghrardad_bvdjh3 = Column("تعداد پرسنل به تفکیک نوع قرارداد - بودجه3",Float)
    tdad_prsnl_bh_tfkyk_nv_ghrardad_dvrh_mshabh = Column("تعداد پرسنل به تفکیک نوع قرارداد - دوره مشابه", Float)
