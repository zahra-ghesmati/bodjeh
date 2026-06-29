from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base
#
class AccountsAndDocumentsReceivable(Base):
    __tablename__ = "Accounts and documents receivable"
    __table_args__ = {"schema": "Report_Main"}
    id = Column(Integer, primary_key=True, autoincrement=True)

    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    bdhkar = Column("بدهکار", NVARCHAR(255))
    mblgh_asnad_dryaftny_srrsyd_shdh = Column("مبلغ اسناد دریافتنی سررسید شده", Float)
    mblgh_asnad_dryaftny_srrsyd_nshdh = Column("مبلغ اسناد دریافتنی سررسید نشده", Float)
    mjmv_asnad_dryaftny = Column("مجموع اسناد دریافتنی",Float)
    mblgh_hsab_dryaftny = Column("مبلغ حساب دریافتنی", Float)
    mjmv_hsabha_v_asnad_dryaftny = Column("مجموع حسابها و اسناد دریافتنی", Float)
