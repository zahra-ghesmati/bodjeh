#برای 8 فرم

from pydantic import BaseModel
from typing import Any


class DynamicRow(BaseModel):
    id: int | None = None
    values: dict[str, Any]


class SaveDynamicFormRequest(BaseModel):
    company: str
    year: str
    month: str
    rows: list[DynamicRow]