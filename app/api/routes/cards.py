from fastapi import APIRouter, Body, Depends, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from app.api.dependencies.database import get_repository
from app.core import config
from app.db.repositories.cards import CardRepository
from app.models.domain.cards import Card
from app.models.schemas.cards import CardBase, CardMatchRequest, CardResponse, CardGetResponse

router = APIRouter()


@router.get("/{board_id}/{position}", response_model=CardGetResponse, name="cards:get-card-detail")
async def retreive_card_value(
    board_id: str,
    position: str,
    card_repo: CardRepository = Depends(get_repository(CardRepository)),
) -> CardBase:
    card_row = await card_repo.get_card_detail(board_id=board_id, position=position)
    return card_row

@router.post("/match-card", name="cards:match-cards")
async def match_cards(
    body: CardMatchRequest,
    card_repo: CardRepository = Depends(get_repository(CardRepository)),
) -> CardBase:
    result = await card_repo.match_Card(first_position=body.first_position, second_position=body.second_position, board_id=body.board_id)
    return result
