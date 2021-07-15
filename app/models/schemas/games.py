from typing import List

from pydantic import BaseModel

from app.models.schemas.cards import Card


class GameBase(BaseModel):
    board_id: str
    click_count: int
    is_finish: bool
    columns: int
    rows: int


class GameCreate(GameBase):
    pass
class GameUpdate(BaseModel):
    board_id: str

class GameInResponse(GameBase):
    id: int
    cards: List[Card] = []

class Game(GameBase):
    id: int
    cards: List[Card] = []

    class Config:
        orm_mode = True
