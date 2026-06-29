from sqlalchemy import Column, String, Integer, DateTime, Boolean, Float
from ..database import Base

class Fund(Base):
    __tablename__ = "Fund"
    __table_args__ = {"schema": "Report_Main"}

    nam_shrkt = Column("نام شرکت", String(255), primary_key=True)
    srmayh = Column("سرمایه", Integer, primary_key=False)
    tdad_sham = Column("تعداد سهام", Integer, primary_key=False)
