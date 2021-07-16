from typing import List

from pydantic import BaseModel


class StatBase(BaseModel):
    user_id: str
    best_click_count: int

class StatUpdate(StatBase):
    pass

class StatInResponse(StatBase):
    id: int

class Stat(StatBase):
    class Config:
        orm_mode = True
