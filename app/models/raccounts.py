from ..database import Base
from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class Raccounts(Base):
    __tablename__ = "R.Accounts"
    __table_args__ = {"schema": "Report_Main"}
    id = Column(Integer, primary_key=True, autoincrement=True)

    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    mjmv_hsabha_v_asnad_dryaftny_tjary_v_ghyr_tjary_vaghy_sal_jary = Column("مجموع حسابها و اسناد دریافتنی تجاری و غیر تجاری - واقعی سال جاری", Float)
    mandh_hsabha_v_asnad_dryaftny_tjary_vaghy_sal_jary = Column("مانده حسابها و اسناد دریافتنی تجاری - واقعی سال جاری", Float)
    mandh_hsabha_v_asnad_dryaftny_ghyr_tjary_vaghy_sal_jary = Column("مانده حسابها و اسناد دریافتنی غیر تجاری - واقعی سال جاری", Float)
    mblgh_tlb_az_rvh_vaghy_sal_jary = Column("مبلغ طلب از گروه - واقعی سال جاری", Float)
    mblgh_tlb_kharj_az_rvh_vaghy_sal_jary = Column("مبلغ طلب خارج از گروه - واقعی سال جاری", Float)
    mjmv_hsabha_v_asnad_dryaftny_tjary_v_ghyr_tjary_dvrh_mshabh = Column("مجموع حسابها و اسناد دریافتنی تجاری و غیر تجاری - دوره مشابه", Float)
    mandh_hsabha_v_asnad_dryaftny_tjary_dvrh_mshabh = Column("مانده حسابها و اسناد دریافتنی تجاری - دوره مشابه", Float)
    mandh_hsabha_v_asnad_dryaftny_ghyr_tjary_dvrh_mshabh = Column("مانده حسابها و اسناد دریافتنی غیر تجاری - دوره مشابه", Float)
    mblgh_tlb_az_rvh_dvrh_mshabh = Column("مبلغ طلب از گروه - دوره مشابه", Float)
    mblgh_tlb_kharj_az_rvh_dvrh_mshabh = Column("مبلغ طلب خارج از گروه - دوره مشابه", Float)
    mjmv_hsabha_v_asnad_dryaftny_tjary_v_ghyr_tjary_bvdjh = Column("مجموع حسابها و اسناد دریافتنی تجاری و غیر تجاری - بودجه", Float)
