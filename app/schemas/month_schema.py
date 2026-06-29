from pydantic import BaseModel


class CreateYearRequest(BaseModel):

    year: str