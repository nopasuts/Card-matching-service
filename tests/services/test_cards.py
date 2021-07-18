import pytest
from unittest import mock

from app.services.cards import get_card_rows, is_cards_match

def test_get_card_rows():
  mock_game_id = 1
  mock_column = 3
  mock_row = 2
  mock_list = [3, 2, 1, 1, 2, 3]
  mock_result = [
    {
      "position": "1x1",
      "is_open": False,
      "game_id": 1,
      "value": 3,
    },
    {
      "position": "1x2",
      "is_open": False,
      "game_id": 1,
      "value": 2,
    },
    {
      "position": "2x1",
      "is_open": False,
      "game_id": 1,
      "value": 1,
    },
    {
      "position": "2x2",
      "is_open": False,
      "game_id": 1,
      "value": 1,
    },
    {
      "position": "3x1",
      "is_open": False,
      "game_id": 1,
      "value": 2,
    },
    {
      "position": "3x2",
      "is_open": False,
      "game_id": 1,
      "value": 3,
    },
  ]
  result = get_card_rows(mock_game_id, mock_column, mock_row, mock_list)
  assert result == mock_result

def test_is_card_match_matched():
  mock_first_card = {
    "value": 1
  }
  mock_second_card = {
    "value": 1
  }
  result = is_cards_match(mock_first_card, mock_second_card)
  assert result == True

def test_is_card_match_not_matched():
  mock_first_card = {
    "value": 1
  }
  mock_second_card = {
    "value": 2
  }
  result = is_cards_match(mock_first_card, mock_second_card)
  assert result == False
