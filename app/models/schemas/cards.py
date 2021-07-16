from pydantic import BaseModel
from typing import Optional


class CardBase(BaseModel):
    position: str
    is_open: bool
    value: int

class CardMatchRequest(BaseModel):
    first_position: str
    second_position: str
    board_id: str

class CardResponse(BaseModel):
    id: int
    position: str
    is_open: bool
    value: Optional[int]
    game_id: Optional[int]

class CardGetResponse(BaseModel):
    id: int
    is_open: bool
    value: int

class Card(CardBase):
    id: int
    game_id: int
    class Config:
        orm_mode = True
