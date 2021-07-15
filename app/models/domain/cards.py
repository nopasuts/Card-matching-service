from app.models.domain.rwmodel import RWModel
from app.models.common import DateTimeModelMixin, IDModelMixin

class Card(IDModelMixin, DateTimeModelMixin, RWModel):
    position: str
    is_open: bool
    value: int
    game_id: int
