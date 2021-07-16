from typing import Optional

from pydantic import BaseModel


class StatBase(BaseModel):
    user_id: str
    best_click_count: int

class StatGetResponse(BaseModel):
    id: int
    user_id: str
    best_click_count: Optional[int] = None

class StatUpdateUserRequest(StatBase):
    pass

class StatUpdateUserResponse(StatGetResponse):
    pass
class StatUpdateGlobalRequest(StatBase):
    pass

class StatUpdateGlobalResponse(StatGetResponse):
    pass

class StatInResponse(StatBase):
    id: int

class Stat(StatBase):
    class Config:
        orm_mode = True
