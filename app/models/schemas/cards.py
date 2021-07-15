from pydantic import BaseModel


class CardBase(BaseModel):
    position: str
    is_open: bool
    value: int


class CardCreate(CardBase):
    pass


class Card(CardBase):
    id: int
    game_id: int

    class Config:
        orm_mode = True
