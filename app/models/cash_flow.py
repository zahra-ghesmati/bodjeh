from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer
)
from ..database import Base

class CashFlow(Base):
    __tablename__ = "Cash Flow"
    __table_args__ = {"schema": "Report_Main"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    shrh = Column("شرح", NVARCHAR(255))
    nvan = Column("عنوان", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    dy = Column("دی", NVARCHAR(255))
    bhmn = Column("بهمن", NVARCHAR(255))
    asfnd = Column("اسفند", NVARCHAR(255))
    frvrdyn = Column("فروردین", NVARCHAR(255))
    ardybhsht = Column("اردیبهشت", NVARCHAR(255))
    khrdad = Column("خرداد", NVARCHAR(255))
    tyr = Column("تیر", NVARCHAR(255))
    mrdad = Column("مرداد", NVARCHAR(255))
    shhryvr = Column("شهریور", NVARCHAR(255))
    mhr = Column("مهر", NVARCHAR(255))
    aban = Column("آبان", NVARCHAR(255))
    azr = Column("آذر", NVARCHAR(255))
    mjmv = Column("مجموع", NVARCHAR(255))
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
