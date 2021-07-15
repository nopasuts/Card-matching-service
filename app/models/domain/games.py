from typing import List

from app.models.domain.rwmodel import RWModel
from app.models.common import DateTimeModelMixin, IDModelMixin

from app.models.domain.cards import Card

class Game(IDModelMixin, DateTimeModelMixin, RWModel):
    board_id: str
    click_count: int
    is_finish: bool
    cards: List[Card] = []
