from fastapi import APIRouter, Body, Depends, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from app.api.dependencies.database import get_repository
from app.core import config
from app.db.repositories.games import GamesRepository
from app.db.repositories.stats import StatRepository
from app.models.domain.games import Game
from app.models.schemas.games import GameInResponse, GameUpdateClickRequest, GameUpdateClickResponse, GameFinishRequest, GameFinishResponse

router = APIRouter()


@router.get("/{board_id}",response_model=GameInResponse, name="games:get-current-game")
async def retreive_current_game(
    board_id: str,
    game_repo: GamesRepository = Depends(get_repository(GamesRepository)),
) -> GameInResponse:
    game_row = await game_repo.get_current_game_by_board_id(board_id=board_id)
    return game_row

@router.post("/",response_model=GameInResponse, name="games:create-new-game")
async def create_new_game(
    game_repo: GamesRepository = Depends(get_repository(GamesRepository)),
) -> GameInResponse:
    game_row = await game_repo.create_game()
    return game_row

@router.put("/click",response_model=GameUpdateClickResponse, name="games:update-click-count")
async def update_game_click_count(
    body: GameUpdateClickRequest,
    game_repo: GamesRepository = Depends(get_repository(GamesRepository)),
) -> GameInResponse:
    result = await game_repo.update_click(board_id=body.board_id)
    return result

@router.post("/finish", response_model=GameFinishResponse, name="games:finish-the-game")
async def finish_the_game(
    body: GameFinishRequest,
    game_repo: GamesRepository = Depends(get_repository(GamesRepository)),
    stat_repo: StatRepository = Depends(get_repository(StatRepository)),
) -> GameInResponse:
    user_row = await stat_repo.get_or_create_user(user_id=body.user_id)
    game_row = await game_repo.finish_game(board_id=body.board_id)
    if user_row["best_click_count"] == None or user_row["best_click_count"] > game_row["click_count"]:
        await stat_repo.update_user_best(user_id=user_row["user_id"], best_click_count=game_row["click_count"])
    await stat_repo.check_and_update_global_best(best_click_count=game_row["click_count"])
    return game_row
