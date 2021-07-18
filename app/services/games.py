from app.core.config import GAME_BOARD_SIZE
import random
from datetime import datetime

def scramble(arrayOfNumber):
  random.shuffle(arrayOfNumber)
  return arrayOfNumber

def get_board_size():
  if GAME_BOARD_SIZE > 3:
    column: int = GAME_BOARD_SIZE
    row: int = GAME_BOARD_SIZE-1
    totalBoardNumber: int = column * row
    arrayNumber = []
    for each in range(totalBoardNumber//2):
      arrayNumber += [each+1, each+1]
    shuffleArrayNumber = scramble(arrayNumber)
    result = {
      "totalBoardNumber": totalBoardNumber,
      "column": column,
      "row": row,
      "shuffleArrayNumber": shuffleArrayNumber,
    }
    return result
  else:
    column: int = 3
    row: int = 2
    totalBoardNumber: int = column * row
    arrayNumber = []
    for each in range(totalBoardNumber//2):
      arrayNumber += [each+1, each+1]
    shuffleArrayNumber = scramble(arrayNumber)
    result = {
      "totalBoardNumber": totalBoardNumber,
      "column": column,
      "row": row,
      "shuffleArrayNumber": shuffleArrayNumber,
    }
    return result

def generate_board_id():
  now = datetime.now()
  dt_string = now.strftime("BOARD-%d%m%YT%H%M%S")
  return dt_string
