from typing import Optional

from app.db.errors import EntityDoesNotExist
from app.db.queries.queries import queries
from app.db.repositories.base import BaseRepository
from app.models.domain.games import Game


class GamesRepository(BaseRepository):
    async def get_current_game_by_game_id(self, *, game_id: str) -> Game:
        game_row = await queries.get_game_info_by_game_id(self.connection, game_id=game_id)
        if game_row:
            return Game(**game_row)

        raise EntityDoesNotExist("game with game id {0} does not exist".format(game_id))

    async def create_game(
        self,
        *,
        game_id: str,
        click_count: int,
    ) -> Game:
        game = Game(game_id=game_id, click_count=click_count)

        async with self.connection.transaction():
            game_row = await queries.create_new_game(
                self.connection,
                game_id=game.game_id,
                click_count=game.click_count,
            )

        return game.copy(update=dict(game_row))

    async def update_game(
        self,
        *,
        game: Game,
        click_count: Optional[int] = None,
    ) -> Game:
        game_in_db = await self.get_current_game_by_game_id(game_id=game.game_id)

        game_in_db.click_count = click_count or game_in_db.click_count

        async with self.connection.transaction():
            game_in_db.updated_at = await queries.update_game_by_game_id(
                self.connection,
                game_id=game.game_id,
                click_count=game.click_count,
            )

        return game_in_db
