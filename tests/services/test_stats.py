import pytest
from unittest import mock

from app.services.stats import generate_user_id
from datetime import datetime

def test_generate_board_id():
  with mock.patch('app.services.stats.datetime') as mock_datetime:
    mock_datetime.now.return_value = datetime(2021, 1, 1)
    mock_datetime.side_effect = lambda *args, **kw: datetime(*args, **kw)

    result = generate_user_id()
    assert result == "USER-01012021T000000"
