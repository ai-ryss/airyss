from fastapi import APIRouter

router = APIRouter(prefix="/git", tags=["git"])


@router.get("/status")
def git_status() -> dict:
    # TODO: implement git status via git service
    return {}
