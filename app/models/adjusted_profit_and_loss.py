from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class AdjustedProfitAndLoss(Base):
    __tablename__ = "Adjusted profit and loss"
    __table_args__ = {"schema": "Report_Main"}
        # id به عنوان کلید اصلی (مطابق دیتابیس جدید)
    id = Column(Integer, primary_key=True, autoincrement=True)
    mblgh_vaghy_sal_jary = Column("مبلغ - واقعی سال جاری", Float)
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    ajza_svd_v_zyan = Column("اجزاء سود و زیان", NVARCHAR(255))
    mblgh_bvdjh = Column("مبلغ - بودجه", Float)
    mblgh_bvdjh2 = Column("مبلغ - بودجه2", Float)
    mblgh_bvdjh3 = Column("مبلغ - بودجه3", Float)
    mblgh_dvrh_mshabh = Column("مبلغ - دوره مشابه",Float)
