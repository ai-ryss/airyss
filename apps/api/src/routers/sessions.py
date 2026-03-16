from fastapi import APIRouter

from src.schemas.session import Session

router = APIRouter(prefix="/sessions", tags=["sessions"])


@router.get("", response_model=list[Session])
def list_sessions() -> list[Session]:
    # TODO: implement session listing via orchestrator service
    return []
