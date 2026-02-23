from pydantic import BaseModel

class DetailsResponse(BaseModel):
    detail: str