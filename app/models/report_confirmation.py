from sqlalchemy import Column, String, Integer, DateTime, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class PeriodLock(Base):
    __tablename__ = "period_locks"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    form_key = Column(String(100), nullable=False) # مثلا: 'admin_costs'
    company = Column(String(200), nullable=False)
    sal_maly = Column(String(20), nullable=False)
    mah = Column(String(20), nullable=False)
    
    budget_approved = Column(Boolean, default=False)
    budget_approved_at = Column(DateTime, nullable=True)
    budget_approved_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    
    actual_approved = Column(Boolean, default=False)
    actual_approved_at = Column(DateTime, nullable=True)
    actual_approved_by = Column(Integer, ForeignKey("users.id"), nullable=True)

    # روابط (اختیاری برای دسترسی راحت‌تر)
    budget_approver = relationship("User", foreign_keys=[budget_approved_by])
    actual_approver = relationship("User", foreign_keys=[actual_approved_by])
