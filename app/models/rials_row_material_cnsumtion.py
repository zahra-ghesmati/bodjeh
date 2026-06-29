from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class RialsRowMaterialCnsumtion(Base):
    __tablename__ = "Rials - Row Material Cnsumtion"
    __table_args__ = {"schema": "Report_Main"}
        # id به عنوان کلید اصلی (مطابق دیتابیس جدید)
    id = Column(Integer, primary_key=True, autoincrement=True)
    mblgh_msrf_mvad_avlyh_vaghy_sal_jary = Column("مبلغ مصرف مواد اولیه - واقعی سال جاری",  Float )
    nam_shrkt = Column("نام شرکت",  NVARCHAR(255) )
    sal_maly = Column("سال مالی",  NVARCHAR(255) )
    mah_zarsh = Column("ماه گزارش",  NVARCHAR(255) )
    mvad_avlyh = Column("مواد اولیه",  NVARCHAR(255) )
    nv_klynkrsyman = Column("نوع کلینکر/سیمان",  NVARCHAR(255) )
    mblgh_msrf_mvad_avlyh_bvdjh = Column("مبلغ مصرف مواد اولیه - بودجه",  Float )
    mblgh_msrf_mvad_avlyh_bvdjh2 = Column("مبلغ مصرف مواد اولیه - بودجه2", Float )
    mblgh_msrf_mvad_avlyh_bvdjh3 = Column("مبلغ مصرف مواد اولیه - بودجه3",  Float )
    mblgh_msrf_mvad_avlyh_dvrh_mshabh = Column("مبلغ مصرف مواد اولیه - دوره مشابه",  Float )
