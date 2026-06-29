from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class HumanResource4(Base):
    __tablename__ = "Human Resource 4"
    __table_args__ = {"schema": "Report_Main"}
            # id به عنوان کلید اصلی (مطابق دیتابیس جدید)
    id = Column(Integer, primary_key=True, autoincrement=True)

    tdad_vrvdy_v_khrvjy_prsnl_vaghy_sal_jary = Column("تعداد ورودی و خروجی پرسنل - واقعی سال جاری", NVARCHAR(255) )
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    vzyt_nyrvy_ansany = Column("وضعیت نیروی انسانی", NVARCHAR(255))
    tdad_vrvdy_v_khrvjy_prsnl_bvdjh = Column("تعداد ورودی و خروجی پرسنل - بودجه", NVARCHAR(255) )
    tdad_vrvdy_v_khrvjy_prsnl_bvdjh2 = Column("تعداد ورودی و خروجی پرسنل - بودجه2", Float)
    tdad_vrvdy_v_khrvjy_prsnl_bvdjh3 = Column("تعداد ورودی و خروجی پرسنل - بودجه3", Float)
    tdad_vrvdy_v_khrvjy_prsnl_dvrh_mshabh = Column("تعداد ورودی و خروجی پرسنل - دوره مشابه", Float)
