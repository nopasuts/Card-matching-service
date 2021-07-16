from fastapi import APIRouter, Body, Depends, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from app.api.dependencies.database import get_repository
from app.core import config
from app.db.repositories.stats import StatRepository
from app.models.domain.stats import Stat
from app.models.schemas.stats import StatInResponse, StatUpdateUserRequest, StatGetResponse, StatUpdateUserResponse, StatUpdateGlobalRequest, StatUpdateGlobalResponse

router = APIRouter()


@router.get("/{user_id}", response_model=StatGetResponse, name="stats:Get-Or-Create-User")
async def retreive_user_info(
    user_id: str,
    stat_repo: StatRepository = Depends(get_repository(StatRepository)),
) -> StatInResponse:
    user_row = await stat_repo.get_or_create_user(user_id=user_id)
    return user_row

@router.put("/", response_model=StatUpdateUserResponse, name="stats:Update-User-Best-Click-Count")
async def update_user_best_count(
    body: StatUpdateUserRequest,
    stat_repo: StatRepository = Depends(get_repository(StatRepository)),
) -> StatInResponse:
    result = await stat_repo.update_user_best(user_id=body.user_id, best_click_count=body.best_click_count)
    return result

@router.put("/global", response_model=StatUpdateGlobalResponse, name="stats:Update-Global-Best-Click-Count")
async def update_global_best_count(
    body: StatUpdateGlobalRequest,
    stat_repo: StatRepository = Depends(get_repository(StatRepository)),
) -> StatInResponse:
    result = await stat_repo.check_and_update_global_best(best_click_count=body.best_click_count)
    return result
