import pytest
from unittest import mock

from app.db.repositories.base import BaseRepository
from app.db.repositories.stats import StatRepository

from app.db.errors import EntityDoesNotExist


@pytest.mark.asyncio
@mock.patch('app.db.repositories.stats.queries.get_user_by_user_id')
async def test_get_or_create_user_get_user_correctly(mock_get_user_by_user_id):
  mock_get_user_by_user_id.return_value = {
    "id": 1
  }

  stat_repo = StatRepository(BaseRepository)

  result = await stat_repo.get_or_create_user(user_id="some-user-id")
  assert result == {
    "id": 1
  }

@pytest.mark.asyncio
@mock.patch('app.db.repositories.stats.queries.create_new_user')
@mock.patch('app.services.stats.generate_user_id')
@mock.patch('app.db.repositories.stats.queries.get_user_by_user_id')
async def test_get_or_create_user_get_user_not_found(mock_get_user_by_user_id, mock_generate_user_id, mock_create_new_user):
  mock_get_user_by_user_id.return_value = None
  mock_generate_user_id.return_value = "some-new-user-id"
  mock_create_new_user.return_value = {
    "id": 1
  }

  stat_repo = StatRepository(BaseRepository)

  await stat_repo.get_or_create_user(user_id="some-user-id")
  assert mock_create_new_user.called

@pytest.mark.asyncio
@mock.patch('app.db.repositories.stats.queries.create_new_user')
@mock.patch('app.services.stats.generate_user_id')
@mock.patch('app.db.repositories.stats.queries.get_user_by_user_id')
async def test_get_or_create_user_get_user_not_found_and_create_new_user(mock_get_user_by_user_id, mock_generate_user_id, mock_create_new_user):
  mock_get_user_by_user_id.return_value = None
  mock_generate_user_id.return_value = "some-new-user-id"
  mock_create_new_user.return_value = {
    "id": 1
  }

  stat_repo = StatRepository(BaseRepository)

  result = await stat_repo.get_or_create_user(user_id="some-user-id")
  assert result == {
    "id": 1
  }

@pytest.mark.asyncio
@mock.patch('app.db.repositories.stats.queries.update_user_best_click_count')
@mock.patch('app.db.repositories.stats.queries.get_user_by_user_id')
async def test_update_user_best_correctly(mock_get_user_by_user_id, mock_update_user_best_click_count):
  mock_get_user_by_user_id.return_value = {
    "id": 1
  }
  mock_update_user_best_click_count.return_value = {
    "id": 1,
    "best_click_count": 10
  }

  stat_repo = StatRepository(BaseRepository)

  result = await stat_repo.update_user_best(user_id="some-user-id", best_click_count=10)
  assert result == {
    "id": 1,
    "best_click_count": 10
  }

@pytest.mark.xfail(raises=EntityDoesNotExist)
@pytest.mark.asyncio
@mock.patch('app.db.repositories.stats.queries.update_user_best_click_count')
@mock.patch('app.db.repositories.stats.queries.get_user_by_user_id')
async def test_update_user_best_not_found(mock_get_user_by_user_id, mock_update_user_best_click_count):
  mock_get_user_by_user_id.return_value = None
  mock_update_user_best_click_count.return_value = {
    "id": 1,
    "best_click_count": 10
  }

  stat_repo = StatRepository(BaseRepository)

  await stat_repo.update_user_best(user_id="some-user-id", best_click_count=10)

@pytest.mark.asyncio
@mock.patch('app.db.repositories.stats.queries.update_global_best_click_count')
@mock.patch('app.db.repositories.stats.queries.get_user_by_user_id')
async def test_check_and_update_global_best_update_global_best_correctly(mock_get_user_by_user_id, mock_update_global_best_click_count):
  mock_get_user_by_user_id.return_value = {
    "id": 1,
    "user_id": "GLOBAL_STAT",
    "best_click_count": 10,
  }
  mock_update_global_best_click_count.return_value = {
    "id": 1,
    "user_id": "GLOBAL_STAT",
    "best_click_count": 9,
  }

  stat_repo = StatRepository(BaseRepository)

  result = await stat_repo.check_and_update_global_best(best_click_count=9)
  assert result == {
    "id": 1,
    "user_id": "GLOBAL_STAT",
    "best_click_count": 9,
  }

@pytest.mark.asyncio
@mock.patch('app.db.repositories.stats.queries.update_global_best_click_count')
@mock.patch('app.db.repositories.stats.queries.get_user_by_user_id')
async def test_check_and_update_global_best_not_less_than_global_best(mock_get_user_by_user_id, mock_update_global_best_click_count):
  mock_get_user_by_user_id.return_value = {
    "id": 1,
    "user_id": "GLOBAL_STAT",
    "best_click_count": 10,
  }
  mock_update_global_best_click_count.return_value = {
    "id": 1,
    "user_id": "GLOBAL_STAT",
    "best_click_count": 10,
  }

  stat_repo = StatRepository(BaseRepository)

  result = await stat_repo.check_and_update_global_best(best_click_count=11)
  assert result == {
    "id": 1,
    "user_id": "GLOBAL_STAT",
    "best_click_count": 10,
  }

@pytest.mark.asyncio
@mock.patch('app.db.repositories.stats.queries.update_global_best_click_count')
@mock.patch('app.db.repositories.stats.queries.get_user_by_user_id')
async def test_check_and_update_global_best_equal_global_best(mock_get_user_by_user_id, mock_update_global_best_click_count):
  mock_get_user_by_user_id.return_value = {
    "id": 1,
    "user_id": "GLOBAL_STAT",
    "best_click_count": 10,
  }
  mock_update_global_best_click_count.return_value = {
    "id": 1,
    "user_id": "GLOBAL_STAT",
    "best_click_count": 10,
  }

  stat_repo = StatRepository(BaseRepository)

  result = await stat_repo.check_and_update_global_best(best_click_count=10)
  assert result == {
    "id": 1,
    "user_id": "GLOBAL_STAT",
    "best_click_count": 10,
  }

@pytest.mark.asyncio
@mock.patch('app.db.repositories.stats.queries.update_global_best_click_count')
@mock.patch('app.db.repositories.stats.queries.get_user_by_user_id')
async def test_check_and_update_global_best_no_global_best_yet(mock_get_user_by_user_id, mock_update_global_best_click_count):
  mock_get_user_by_user_id.return_value = {
    "id": 1,
    "user_id": "GLOBAL_STAT",
    "best_click_count": None,
  }
  mock_update_global_best_click_count.return_value = {
    "id": 1,
    "user_id": "GLOBAL_STAT",
    "best_click_count": 10,
  }

  stat_repo = StatRepository(BaseRepository)

  result = await stat_repo.check_and_update_global_best(best_click_count=10)
  assert result == {
    "id": 1,
    "user_id": "GLOBAL_STAT",
    "best_click_count": 10,
  }