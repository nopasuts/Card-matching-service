from typing import List

from app.models.domain.rwmodel import RWModel
from app.models.common import DateTimeModelMixin, IDModelMixin

class Stat(IDModelMixin, DateTimeModelMixin, RWModel):
    user_id: str
    best_click_count: int
