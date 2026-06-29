from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class BalanceSheet(Base):
    __tablename__ = "Balance Sheet"
    __table_args__ = {"schema": "Report_Main"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    dr_tarykh_payan_mah_sal_jary = Column("در تاریخ پایان ماه سال جاری", Float)
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    shrh = Column("شرح", NVARCHAR(255))
    tbghh_bndy = Column("طبقه بندی", NVARCHAR(255))
    dr_tarykh_payan_mah_sal_ghbl = Column("در تاریخ پایان ماه سال قبل", Float)
