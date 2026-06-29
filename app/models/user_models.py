from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    users = relationship("User", back_populates="role")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"))
    full_name = Column(String(200))
    is_active = Column(Boolean, default=True)
    
    role = relationship("Role", back_populates="users")
    companies = relationship("UserCompany", back_populates="user")

class UserCompany(Base):
    __tablename__ = "user_companies"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    company_name = Column(String(200), primary_key=True)
    user = relationship("User", back_populates="companies")
