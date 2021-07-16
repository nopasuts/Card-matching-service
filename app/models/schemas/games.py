from typing import List

from pydantic import BaseModel

from app.models.schemas.cards import CardResponse


class GameBase(BaseModel):
    board_id: str
    click_count: int
    is_finish: bool
    columns: int
    rows: int

class GameUpdateClickRequest(BaseModel):
    board_id: str
class GameUpdateClickResponse(BaseModel):
    id: int

class GameInResponse(GameBase):
    id: int
    cards: List[CardResponse] = []

class GameFinishRequest(BaseModel):
    board_id: str
    user_id: str
class GameFinishResponse(GameInResponse):
    pass

class Game(GameBase):
    id: int
    cards: List[CardResponse] = []

    class Config:
        orm_mode = True
