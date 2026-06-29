from ..database import Base
from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class Salary(Base):
    __tablename__ = "Salary"
    __table_args__ = {"schema": "Report_Main"}
    id = Column(Integer, primary_key=True, autoincrement=True)

    dstmzd_mstghym_vaghy_sal_jary = Column("دستمزد مستقیم - واقعی سال جاری", Float)
    dstmzd_srbar_vaghy_sal_jary = Column("دستمزد سربار - واقعی سال جاری", Float)
    dstmzd_adary_mvmy_vaghy_sal_jary = Column("دستمزد اداری عمومی - واقعی سال جاری", Float)
    dstmzd_frvsh_vaghy_sal_jary = Column("دستمزد فروش - واقعی سال جاری", Float)
    mjmv_dstmzd_vaghy_sal_jary = Column("مجموع دستمزد - واقعی سال جاری", Float)
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    ajza_hzynh_prsnly = Column("اجزاء هزینه پرسنلی", NVARCHAR(255))
    dstmzd_mstghym_bvdjh = Column("دستمزد مستقیم - بودجه", Float)
    dstmzd_mstghym_bvdjh2 = Column("دستمزد مستقیم - بودجه2", Float)
    dstmzd_mstghym_bvdjh3 = Column("دستمزد مستقیم - بودجه3", Float)
    dstmzd_mstghym_dvrh_mshabh = Column("دستمزد مستقیم - دوره مشابه", Float)
    dstmzd_srbar_bvdjh = Column("دستمزد سربار - بودجه", Float)
    dstmzd_srbar_bvdjh2 = Column("دستمزد سربار - بودجه2", Float)
    dstmzd_srbar_bvdjh3 = Column("دستمزد سربار - بودجه3", Float)
    dstmzd_srbar_dvrh_mshabh = Column("دستمزد سربار - دوره مشابه", Float)
    dstmzd_adary_mvmy_bvdjh = Column("دستمزد اداری عمومی - بودجه", Float)
    dstmzd_adary_mvmy_bvdjh2 = Column("دستمزد اداری عمومی - بودجه2", Float)
    dstmzd_adary_mvmy_bvdjh3 = Column("دستمزد اداری عمومی - بودجه3", Float)
    dstmzd_adary_mvmy_dvrh_mshabh = Column("دستمزد اداری عمومی - دوره مشابه", Float)
    dstmzd_frvsh_bvdjh = Column("دستمزد فروش - بودجه", Float)
    dstmzd_frvsh_bvdjh2 = Column("دستمزد فروش - بودجه2", Float)
    dstmzd_frvsh_bvdjh3 = Column("دستمزد فروش - بودجه3", Float)
    dstmzd_frvsh_dvrh_mshabh = Column("دستمزد فروش - دوره مشابه", Float)
    mjmv_dstmzd_bvdjh = Column("مجموع دستمزد - بودجه", Float)
    mjmv_dstmzd_bvdjh2 = Column("مجموع دستمزد - بودجه2", Float)
    mjmv_dstmzd_bvdjh3 = Column("مجموع دستمزد - بودجه3", Float)
    mjmv_dstmzd_dvrh_mshabh = Column("مجموع دستمزد - دوره مشابه", Float)
