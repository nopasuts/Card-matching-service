import pytest
from unittest import mock

from app.db.repositories.base import BaseRepository
from app.db.repositories.games import GamesRepository

from app.db.errors import EntityDoesNotExist


@pytest.mark.asyncio
@mock.patch('app.db.repositories.games.queries.get_cards_by_game_id')
@mock.patch('app.db.repositories.games.queries.get_game_info_by_board_id')
async def test_get_current_game_by_board_id_correctly(mock_get_game_row, mock_get_cards_by_game_id):
  mock_return_game_row = {
    "id": 1
  }
  mock_return_card_rows = [
    {
    "position": "1x1",
    "value": 1
    },
    {
    "position": "1x2",
    "value": 1
    }
  ]
  mock_result = {
    "id": 1,
    "cards": mock_return_card_rows
  }

  game_repo = GamesRepository(BaseRepository)
  mock_get_game_row.return_value = mock_return_game_row
  mock_get_cards_by_game_id.return_value = mock_return_card_rows

  result = await game_repo.get_current_game_by_board_id(board_id="some-board-id")
  assert result == mock_result

@pytest.mark.xfail(raises=EntityDoesNotExist)
@pytest.mark.asyncio
@mock.patch('app.db.repositories.games.queries.get_cards_by_game_id')
@mock.patch('app.db.repositories.games.queries.get_game_info_by_board_id')
async def test_get_current_game_by_board_id_not_found(mock_get_game_row, mock_get_cards_by_game_id):
  mock_return_game_row = None
  mock_return_card_rows = [
    {
    "position": "1x1",
    "value": 1
    },
    {
    "position": "1x2",
    "value": 1
    }
  ]
  mock_result = {
    "id": 1,
    "cards": mock_return_card_rows
  }

  game_repo = GamesRepository(BaseRepository)
  mock_get_game_row.return_value = mock_return_game_row
  mock_get_cards_by_game_id.return_value = mock_return_card_rows

  result = await game_repo.get_current_game_by_board_id(board_id="some-board-id")
  assert result == mock_result

@pytest.mark.asyncio
@mock.patch('app.db.repositories.games.queries.create_new_game')
@mock.patch('app.db.repositories.games.queries.create_new_cards')
@mock.patch('app.services.games.generate_board_id')
@mock.patch('app.services.games.get_board_size')
@mock.patch('app.db.repositories.games.GamesRepository.connection')
@mock.patch('app.db.repositories.games.queries.get_cards_by_game_id')
@mock.patch('app.db.repositories.games.GamesRepository.get_current_game_by_board_id')
async def test_create_game_correctly(mock_get_game_row, mock_get_cards_by_game_id, mock_self_connection, mock_get_board_size, mock_generate_board_id, mock_create_new_cards, mock_create_new_game):
  mock_return_game_row = {
    "id": 1
  }
  mock_return_card_rows = [
    {
    "position": "1x1",
    "value": 1
    },
    {
    "position": "1x2",
    "value": 1
    }
  ]

  game_repo = GamesRepository(BaseRepository)
  mock_get_game_row.return_value = mock_return_game_row
  mock_get_cards_by_game_id.return_value = mock_return_card_rows
  mock_get_board_size.return_value = {
    "totalBoardNumber": 12,
    "column": 4,
    "row": 5,
    "shuffleArrayNumber": [1, 3, 2, 1, 3],
  }
  mock_generate_board_id.return_value = "BOARD-some-datetime"
  mock_create_new_cards.return_value = None
  mock_create_new_game.return_value = {
    "id": 1
  }

  result = await game_repo.create_game()
  assert result == mock_return_game_row

@pytest.mark.asyncio
@mock.patch('app.db.repositories.games.queries.update_game_click_count')
@mock.patch('app.db.repositories.games.GamesRepository.connection')
@mock.patch('app.db.repositories.games.GamesRepository.get_current_game_by_board_id')
async def test_update_game_correctly(mock_get_current_game_by_board_id, mock_self_connection, mock_update_game_click_count):
  mock_get_current_game_by_board_id.return_value = {
    "id": 1,
    "click_count": 0,
  }
  mock_update_game_click_count.return_value = {
    "id": 1,
    "click_count": 1,
  }
  game_repo = GamesRepository(BaseRepository)
  result = await game_repo.update_click("some-board-id")
  assert result == {
    "id": 1,
    "click_count": 1,
  }

@pytest.mark.xfail(raises=EntityDoesNotExist)
@pytest.mark.asyncio
@mock.patch('app.db.repositories.games.queries.update_game_click_count')
@mock.patch('app.db.repositories.games.GamesRepository.connection')
@mock.patch('app.db.repositories.games.GamesRepository.get_current_game_by_board_id')
async def test_update_game_not_found(mock_get_current_game_by_board_id, mock_self_connection, mock_update_game_click_count):
  mock_get_current_game_by_board_id.return_value = None
  mock_update_game_click_count.return_value = {
    "id": 1,
    "click_count": 1,
  }
  game_repo = GamesRepository(BaseRepository)
  await game_repo.update_click("some-board-id")

@pytest.mark.asyncio
@mock.patch('app.db.repositories.games.queries.finish_game')
@mock.patch('app.db.repositories.games.GamesRepository.connection')
@mock.patch('app.db.repositories.games.GamesRepository.get_current_game_by_board_id')
async def test_finish_game_correctly(mock_get_current_game_by_board_id, mock_self_connection, mock_finish_game):
  mock_get_current_game_by_board_id.return_value = {
    "id": 1,
  }
  mock_finish_game.return_value = {
    "id": 1,
  }
  game_repo = GamesRepository(BaseRepository)
  result = await game_repo.finish_game("some-board-id")
  assert result == {
    "id": 1,
  }

@pytest.mark.xfail(raises=EntityDoesNotExist)
@pytest.mark.asyncio
@mock.patch('app.db.repositories.games.queries.finish_game')
@mock.patch('app.db.repositories.games.GamesRepository.connection')
@mock.patch('app.db.repositories.games.GamesRepository.get_current_game_by_board_id')
async def test_finish_game_not_found(mock_get_current_game_by_board_id, mock_self_connection, mock_finish_game):
  mock_get_current_game_by_board_id.return_value = None
  mock_finish_game.return_value = {
    "id": 1,
  }
  game_repo = GamesRepository(BaseRepository)
  await game_repo.finish_game("some-board-id")