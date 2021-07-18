from typing import Optional

from app.db.errors import EntityDoesNotExist
from app.db.queries.queries import queries
from app.db.repositories.base import BaseRepository
from app.models.domain.games import Game

from app.services.games import get_board_size, generate_board_id
from app.services.cards import get_card_rows


class GamesRepository(BaseRepository):
    async def get_current_game_by_board_id(self, *, board_id: str) -> Game:
        game_row_raw = await queries.get_game_info_by_board_id(self.connection, board_id=board_id)
        if game_row_raw:
            game_row = dict(game_row_raw)
            cards_list = await queries.get_cards_by_game_id(self.connection, game_id=game_row["id"])
            game_row["cards"] = cards_list
            return game_row

        raise EntityDoesNotExist("game with board id {0} does not exist".format(board_id))

    async def create_game(
        self,
    ) -> Game:
        boardInfo = get_board_size()
        board_id = generate_board_id()
        game = Game(board_id=board_id, click_count=0, is_finish=False, columns=boardInfo["column"], rows=boardInfo["row"])

        async with self.connection.transaction():
            game_row = await queries.create_new_game(
                self.connection,
                board_id=game.board_id,
                click_count=game.click_count,
                is_finish=game.is_finish,
                columns=boardInfo["column"],
                rows=boardInfo["row"],
            )
            cards_info = get_card_rows(
                game_id=game_row["id"],
                column=boardInfo["column"],
                row=boardInfo["row"],
                shuffleArrayNumber=boardInfo["shuffleArrayNumber"]
            )
            await queries.create_new_cards(
                self.connection,
                cards_info
            )
            game_detail = await self.get_current_game_by_board_id(board_id=board_id)

        return dict(game_detail)

    async def update_click(
        self,
        board_id: str
    ) -> Game:
        game_row_raw = await self.get_current_game_by_board_id(board_id=board_id)

        if game_row_raw:
            game_row = dict(game_row_raw)

            click_count = game_row["click_count"] + 1

            async with self.connection.transaction():
                updated_game_row = await queries.update_game_click_count(
                    self.connection,
                    board_id=board_id,
                    click_count=click_count,
                )

            return dict(updated_game_row)

        raise EntityDoesNotExist("game with board id {0} does not exist".format(board_id))

    async def finish_game(
        self,
        board_id: str,
    ) -> Game:
        game_row_raw = await self.get_current_game_by_board_id(board_id=board_id)

        if game_row_raw:
            game_row = dict(game_row_raw)

            async with self.connection.transaction():
                await queries.finish_game(
                    self.connection,
                    board_id=board_id,
                    is_finish=True,
                )

            return dict(game_row)

        raise EntityDoesNotExist("game with board id {0} does not exist".format(board_id))
