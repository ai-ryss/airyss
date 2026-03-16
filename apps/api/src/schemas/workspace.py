from pydantic import BaseModel


class Workspace(BaseModel):
    id: str
    project_id: str
    status: str
