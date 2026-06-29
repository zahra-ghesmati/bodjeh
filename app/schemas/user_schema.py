from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    username: str
    password: str
    full_name: str | None = None
    role_id: int
    company_name: str | None = None
    is_active: bool = True


class UserUpdate(BaseModel):
    username: str
    full_name: str | None = None
    role_id: int
    company_name: str | None = None
    is_active: bool = True
    password: Optional[str] = None