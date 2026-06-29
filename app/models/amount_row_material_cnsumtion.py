from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class AmountRowMaterialCnsumtion(Base):
    __tablename__ = "Amount - Row Material Cnsumtion"
    __table_args__ = {"schema": "Report_Main"}
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    mghdar_msrf_mvad_avlyh_vaghy_sal_jary = Column("مقدار مصرف مواد اولیه - واقعی سال جاری", Float)
    rdyf = Column("ردیف", Integer )
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    mvad_avlyh = Column("مواد اولیه",  NVARCHAR(255) )
    nv_klynkrsyman = Column("نوع کلینکر/سیمان",  NVARCHAR(255) )
    mghdar_msrf_mvad_avlyh_bvdjh = Column("مقدار مصرف مواد اولیه - بودجه", Float)
    mghdar_msrf_mvad_avlyh_bvdjh2 = Column("مقدار مصرف مواد اولیه - بودجه2", Float)
    mghdar_msrf_mvad_avlyh_bvdjh3 = Column("مقدار مصرف مواد اولیه - بودجه3", Float)
    mghdar_msrf_mvad_avlyh_dvrh_mshabh = Column("مقدار مصرف مواد اولیه - دوره مشابه", Float)


