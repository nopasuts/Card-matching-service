from typing import Optional

from app.db.errors import EntityDoesNotExist
from app.db.queries.queries import queries
from app.db.repositories.base import BaseRepository
from app.models.domain.games import Game

from app.services.games import get_board_size, generate_board_id
from app.services.cards import get_card_rows


class GamesRepository(BaseRepository):
    async def get_current_game_by_board_id(self, *, board_id: str) -> Game:
        game_row = await queries.get_game_info_by_board_id(self.connection, board_id=board_id)
        if game_row:
            return Game(**game_row)

        raise EntityDoesNotExist("game with board id {0} does not exist".format(board_id))

    async def create_game(
        self,
    ) -> Game:
        boardInfo = get_board_size()
        board_id = generate_board_id()
        card_rows = get_card_rows(
            board_id=board_id,
            column=boardInfo["column"],
            row=boardInfo["row"],
            shuffleArrayNumber=boardInfo["shuffleArrayNumber"]
        )
        print(card_rows)
        game = Game(board_id=board_id, click_count=0, is_finish=False)

        async with self.connection.transaction():
            game_row = await queries.create_new_game(
                self.connection,
                board_id=game.board_id,
                click_count=game.click_count,
                is_finish=game.is_finish,
            )

        return game.copy(update=dict(game_row))

    async def update_game(
        self,
        *,
        game: Game,
        click_count: Optional[int] = None,
    ) -> Game:
        game_in_db = await self.get_current_game_by_board_id(board_id=game.board_id)

        game_in_db.click_count = click_count or game_in_db.click_count

        async with self.connection.transaction():
            game_in_db.updated_at = await queries.update_game_by_board_id(
                self.connection,
                board_id=game.board_id,
                click_count=game.click_count,
            )

        return game_in_db
