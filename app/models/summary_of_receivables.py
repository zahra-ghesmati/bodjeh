from sqlalchemy import (
    Column,
    NVARCHAR,
    Integer,
    Float
)
from ..database import Base

class SummaryOfReceivables(Base):
    __tablename__ = "Summary of receivables"
    __table_args__ = {"schema": "Report_Main"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    payan_mah_jary = Column("پایان ماه جاری", Float)
    nam_shrkt = Column("نام شرکت", NVARCHAR(255))
    sal_maly = Column("سال مالی", NVARCHAR(255))
    mah_zarsh = Column("ماه گزارش", NVARCHAR(255))
    shrh = Column("شرح", NVARCHAR(255))
    abtday_sal_maly_jary = Column("ابتدای سال مالی جاری", Float)
    payan_mah_jary_sal_ghbl = Column("پایان ماه جاری سال قبل", Float)
