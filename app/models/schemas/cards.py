from pydantic import BaseModel


class CardBase(BaseModel):
    position: str
    is_open: bool
    value: int

class CardMatch(BaseModel):
    first_position: str
    second_position: str
    board_id: str


class Card(CardBase):
    id: int
    game_id: int

    class Config:
        orm_mode = True
