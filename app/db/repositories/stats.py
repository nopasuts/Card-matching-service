from typing import Optional

from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.expression import null

from app.db.errors import EntityDoesNotExist
from app.db.queries.queries import queries
from app.db.repositories.base import BaseRepository
from app.models.domain.stats import Stat

from app.services.stats import generate_user_id

class StatRepository(BaseRepository):
    async def get_or_create_user(self, *, user_id: str) -> Stat:
      user_row = await queries.get_user_by_user_id(self.connection, user_id=user_id)
      if user_row:
          return dict(user_row)
      new_user_id = generate_user_id()
      user_created = await queries.create_new_user(self.connection, user_id=new_user_id, best_click_count=None)
      return dict(user_created)

    async def update_user_best(self, *, user_id: str, best_click_count: int) -> Stat:
      user_row = await queries.get_user_by_user_id(self.connection, user_id=user_id)
      if user_row:
        updated_user = await queries.update_user_best_click_count(self.connection, user_id=user_id, best_click_count=best_click_count)
        return dict(updated_user)

      raise EntityDoesNotExist("user with user id {0} does not exist".format(user_id))

    async def check_and_update_global_best(self, *, best_click_count: int) -> Stat:
      global_user_id = 'GLOBAL_STAT'
      global_user_row = await queries.get_user_by_user_id(self.connection, user_id=global_user_id)
      if  global_user_row["best_click_count"] == None or global_user_row["best_click_count"] > best_click_count:
        updated_global = await queries.update_global_best_click_count(self.connection, best_click_count=best_click_count)
        return dict(updated_global)
      return dict(global_user_row)
