from pydantic import BaseModel
from typing import List

class UserInDB(BaseModel):
    id: int
    username: str
    role: str
    companies: List[str]

class Token(BaseModel):
    access_token: str
    token_type: str
