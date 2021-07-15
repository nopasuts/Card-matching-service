from fastapi import APIRouter, Body, Depends, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from app.api.dependencies.database import get_repository
from app.core import config
from app.db.repositories.games import GamesRepository
from app.models.domain.games import Game
from app.models.schemas.games import GameInResponse

router = APIRouter()


@router.get("/{board_id}", response_model=GameInResponse, name="games:get-current-game")
async def retreive_current_game(
    board_id: str,
    game_repo: GamesRepository = Depends(get_repository(GamesRepository)),
) -> GameInResponse:
    game_row = await game_repo.get_current_game_by_board_id(board_id=board_id)
    return GameInResponse(
        game=game_row
    )

@router.post("/", name="games:create-new-game")
async def retreive_current_game(
    game_repo: GamesRepository = Depends(get_repository(GamesRepository)),
) -> GameInResponse:
    game_row = await game_repo.create_game()
    return game_row
