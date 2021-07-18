import pytest
import os
from unittest import mock
from app.services.games import scramble, get_board_size, generate_board_id
from datetime import datetime

def mock_shuffle(value):
  return [3, 2, 1]

def mock_scramble(value):
  return [1, 2, 3, 2, 1]

def test_scramble_correctly():
  with mock.patch('random.shuffle', return_value=[3, 2, 1]) as mock_random:
    mock_array = [1, 2, 3]
    scramble(mock_array)
    assert mock_random.called

def test_get_board_size():
  with mock.patch('app.services.games.scramble', mock_scramble):
    mock_result = {
      "totalBoardNumber": 12,
      "column": 4,
      "row": 3,
      "shuffleArrayNumber": [1, 2, 3, 2, 1],
    }
    result = get_board_size()
    assert result == mock_result

def test_generate_board_id():
  with mock.patch('app.services.games.datetime') as mock_datetime:
    mock_datetime.now.return_value = datetime(2021, 1, 1)
    mock_datetime.side_effect = lambda *args, **kw: datetime(*args, **kw)

    result = generate_board_id()
    assert result == "BOARD-01012021T000000"
