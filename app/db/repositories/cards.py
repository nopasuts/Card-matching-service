from typing import Optional

from app.db.errors import EntityDoesNotExist
from app.db.queries.queries import queries
from app.db.repositories.base import BaseRepository
from app.models.domain.cards import Card

from app.services.cards import is_cards_match

class CardRepository(BaseRepository):
    async def get_card_detail(self, *, board_id: str, position: str) -> Card:
        game_row_raw = await queries.get_game_info_by_board_id(self.connection, board_id=board_id)
        if game_row_raw:
            game_row = dict(game_row_raw)
            card_row = await queries.get_card_by_position(self.connection, position=position, game_id=game_row["id"])
            return dict(card_row)

        raise EntityDoesNotExist("card with position {0} does not exist".format(position))

    async def match_Card(
        self,
        *,
        board_id: str,
        first_position: str,
        second_position: str,
    ) -> Card:
        game_row_raw = await queries.get_game_info_by_board_id(self.connection, board_id=board_id)
        if game_row_raw:
          game_row = dict(game_row_raw)
          game_id = game_row["id"]
          first_card_row = await queries.get_card_by_position(self.connection, position=first_position, game_id=game_id)
          second_card_row = await queries.get_card_by_position(self.connection, position=second_position, game_id=game_id)
          if (is_cards_match(dict(first_card_row), dict(second_card_row))):
            async with self.connection.transaction():
              await queries.update_is_open_card(position=first_position, game_id=game_id, is_open=True)
              await queries.update_is_open_card(position=second_position, game_id=game_id, is_open=True)
              return "SUCCESS"

        return "UNSUCCESS"
