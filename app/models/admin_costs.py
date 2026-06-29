from sqlalchemy import Column, String, Integer, Float, NVARCHAR
from ..database import Base

class AdminCosts(Base):
    __tablename__ = "Admin costs"
    __table_args__ = {"schema": "Report_Main"}

    # id به عنوان کلید اصلی (مطابق دیتابیس جدید)
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # ستون‌های متنی حالا NVARCHAR هستند
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    ajza_hzynh_adary_mvmy_v_frvsh = Column("اجزاء هزینه اداری عمومی و فروش", NVARCHAR(255))
    mhl_hzynh = Column("محل هزینه", NVARCHAR(255))
    
    # ستون‌های عددی حالا FLOAT هستند
    hzynh_adary_v_frvsh_vaghy_sal_jary = Column("هزینه اداری و فروش - واقعی سال جاری", Float)
    hzynh_adary_v_frvsh_bvdjh = Column("هزینه اداری و فروش - بودجه", Float)
    hzynh_adary_v_frvsh_bvdjh2 = Column("هزینه اداری و فروش - بودجه2", Float)
    hzynh_adary_v_frvsh_bvdjh3 = Column("هزینه اداری و فروش - بودجه3", Float)
    hzynh_adary_v_frvsh_dvrh_mshabh = Column("هزینه اداری و فروش - دوره مشابه", Float)
