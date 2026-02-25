from pydantic import BaseModel


class FormatBase(BaseModel):
    type: str


class FormatCreate(FormatBase):
    pass


class FormatRead(FormatBase):
    id: int

    class Config:
        orm_mode = True
