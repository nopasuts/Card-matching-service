from fastapi import APIRouter, Body, Depends, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from app.api.dependencies.database import get_repository
from app.core import config
from app.db.repositories.games import GamesRepository
from app.models.domain.games import Game
from app.models.schemas.games import GameInResponse, GameUpdate

router = APIRouter()


@router.get("/{board_id}", name="games:get-current-game")
async def retreive_current_game(
    board_id: str,
    game_repo: GamesRepository = Depends(get_repository(GamesRepository)),
) -> GameInResponse:
    game_row = await game_repo.get_current_game_by_board_id(board_id=board_id)
    return game_row

@router.post("/", name="games:create-new-game")
async def create_new_game(
    game_repo: GamesRepository = Depends(get_repository(GamesRepository)),
) -> GameInResponse:
    game_row = await game_repo.create_game()
    return game_row

@router.put("/click", name="games:update-click-count")
async def update_game_click_count(
    body: GameUpdate,
    game_repo: GamesRepository = Depends(get_repository(GamesRepository)),
) -> GameInResponse:
    result = await game_repo.update_click(board_id=body.board_id)
    return result
