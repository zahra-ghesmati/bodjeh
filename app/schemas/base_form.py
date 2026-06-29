from pydantic import BaseModel
from typing import List, Optional

class RowItem(BaseModel):
    id: int | None = None

    dimension1: str | None = None
    dimension2: str | None = None
    dimension3: str | None = None

    budget: float | None = None
    actual: float | None = None

    
class SaveFormRequest(BaseModel):
    company: str
    year: str
    month: str
    rows: List[RowItem]