from sqlalchemy import Column, String, Integer, DateTime, Boolean, Float
from ..database import Base

class FullDimdatePb(Base):
    __tablename__ = "Full_DimDate_PB"
    __table_args__ = {"schema": "Report_Main"}

    miladi = Column("Miladi", String(255), primary_key=False)
    jalali_1 = Column("Jalali_1", String(255), primary_key=False)
    jalali_2 = Column("Jalali_2", String(255), primary_key=False)
    jalali_3 = Column("Jalali_3", String(255), primary_key=False)
    miladi_1 = Column("Miladi (#1)", String(255), primary_key=False)
    jyear = Column("jyear", String(255), primary_key=False)
    mmonthn = Column("mmonthN", Integer, primary_key=False)
    jmonthn = Column("jmonthN", Integer, primary_key=False)
    mmontht = Column("mmonthT", String(255), primary_key=False)
    jmontht = Column("jmonthT", String(255), primary_key=False)
    mnime = Column("mnime", String(255), primary_key=False)
    jnime = Column("jnime", String(255), primary_key=False)
    jquartern = Column("JquarterN", Integer, primary_key=False)
    jquartert = Column("JQuarterT", String(255), primary_key=False)
    mquartern = Column("MquarterN", Integer, primary_key=False)
    jweekday = Column("JWeekDay", String(255), primary_key=False)
    mweekday = Column("MWeekDay", String(255), primary_key=False)
    mweeknum = Column("MWeekNum", Integer, primary_key=False)
    jweeknum = Column("JWeekNum", Integer, primary_key=False)
