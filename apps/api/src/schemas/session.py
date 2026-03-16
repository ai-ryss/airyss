from pydantic import BaseModel


class Session(BaseModel):
    id: str
    status: str
