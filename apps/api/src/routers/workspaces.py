from fastapi import APIRouter

from src.schemas.workspace import Workspace

router = APIRouter(prefix="/workspaces", tags=["workspaces"])


@router.get("", response_model=list[Workspace])
def list_workspaces() -> list[Workspace]:
    # TODO: implement workspace listing via workspace service
    return []
