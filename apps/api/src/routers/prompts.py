from fastapi import APIRouter

router = APIRouter(prefix="/prompts", tags=["prompts"])


@router.get("")
def list_prompts() -> list:
    # TODO: implement prompt template listing
    return []
