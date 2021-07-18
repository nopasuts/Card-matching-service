import pytest
from unittest import mock

from app.db.repositories.base import BaseRepository
from app.db.repositories.cards import CardRepository

from app.db.errors import EntityDoesNotExist


@pytest.mark.asyncio
@mock.patch('app.db.repositories.cards.queries.get_card_by_position')
@mock.patch('app.db.repositories.cards.queries.get_game_info_by_board_id')
async def test_get_card_detail_correctly(mock_get_game_row, mock_get_card_by_position):
  mock_return_game_row = {
    "id": 1
  }
  mock_return_card_row = {
    "position": "1x1",
    "value": 1
  }

  card_repo = CardRepository(BaseRepository)
  mock_get_game_row.return_value = mock_return_game_row
  mock_get_card_by_position.return_value = mock_return_card_row

  result = await card_repo.get_card_detail(board_id="some-board-id", position="1x1")
  assert result == mock_return_card_row

@pytest.mark.xfail(raises=EntityDoesNotExist)
@pytest.mark.asyncio
@mock.patch('app.db.repositories.cards.queries.get_card_by_position')
@mock.patch('app.db.repositories.cards.queries.get_game_info_by_board_id')
async def test_get_card_detail_not_found(mock_get_game_row, mock_get_card_by_position):
  mock_return_game_row = None
  mock_return_card_row = None

  card_repo = CardRepository(BaseRepository)
  mock_get_game_row.return_value = mock_return_game_row
  mock_get_card_by_position.return_value = mock_return_card_row

  await card_repo.get_card_detail(board_id="some-board-id", position="1x1")


@pytest.mark.asyncio
@mock.patch('app.db.repositories.cards.CardRepository.connection')
@mock.patch('app.db.repositories.cards.queries.update_is_open_card')
@mock.patch('app.db.repositories.cards.queries.get_card_by_position')
@mock.patch('app.db.repositories.cards.queries.get_game_info_by_board_id')
async def test_match_cards_correctly(mock_get_game_row, mock_get_card_by_position, mock_update_is_open_card, mock_self_connection):
  mock_return_game_row = {
    "id": 1
  }
  mock_return_card_row = {
    "value": 1
  }
  mock_return_update_open_card = {
    "is_open": True
  }

  card_repo = CardRepository(BaseRepository)
  mock_get_game_row.return_value = mock_return_game_row
  mock_get_card_by_position.return_value = mock_return_card_row
  mock_update_is_open_card.return_value = mock_return_update_open_card

  result = await card_repo.match_Card(board_id="some-board-id", first_position="1x1", second_position="1x2")
  assert result == "SUCCESS"

@pytest.mark.asyncio
@mock.patch('app.db.repositories.cards.CardRepository.connection')
@mock.patch('app.db.repositories.cards.queries.update_is_open_card')
@mock.patch('app.db.repositories.cards.queries.get_card_by_position')
@mock.patch('app.db.repositories.cards.queries.get_game_info_by_board_id')
async def test_match_cards_not_match(mock_get_game_row, mock_get_card_by_position, mock_update_is_open_card, mock_self_connection):
  mock_return_game_row = {
    "id": 1
  }
  mock_return_card_row_first = {
    "value": 1
  }
  mock_return_card_row_second = {
    "value": 2
  }
  mock_return_update_open_card = {
    "is_open": True
  }

  card_repo = CardRepository(BaseRepository)
  mock_get_game_row.return_value = mock_return_game_row
  mock_get_card_by_position.side_effect = [mock_return_card_row_first, mock_return_card_row_second]
  mock_update_is_open_card.return_value = mock_return_update_open_card

  result = await card_repo.match_Card(board_id="some-board-id", first_position="1x1", second_position="1x2")
  assert result == "UNSUCCESS"

@pytest.mark.asyncio
@mock.patch('app.db.repositories.cards.CardRepository.connection')
@mock.patch('app.db.repositories.cards.queries.update_is_open_card')
@mock.patch('app.db.repositories.cards.queries.get_card_by_position')
@mock.patch('app.db.repositories.cards.queries.get_game_info_by_board_id')
async def test_match_cards_game_not_found(mock_get_game_row, mock_get_card_by_position, mock_update_is_open_card, mock_self_connection):
  mock_return_game_row = None
  mock_return_card_row_first = {
    "value": 1
  }
  mock_return_card_row_second = {
    "value": 2
  }
  mock_return_update_open_card = {
    "is_open": True
  }

  card_repo = CardRepository(BaseRepository)
  mock_get_game_row.return_value = mock_return_game_row
  mock_get_card_by_position.side_effect = [mock_return_card_row_first, mock_return_card_row_second]
  mock_update_is_open_card.return_value = mock_return_update_open_card

  result = await card_repo.match_Card(board_id="some-board-id", first_position="1x1", second_position="1x2")
  assert result == "UNSUCCESS"
