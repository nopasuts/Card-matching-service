from typing import List

def get_card_rows(board_id: str, column: int, row: int, shuffleArrayNumber: List[int]):
  order = 0
  cards = []
  for eachCol in range(column):
    for eachRow in range(row):
      position = "{0}x{1}".format(eachCol, eachRow)
      is_open = False
      value = shuffleArrayNumber[order]
      order += 1
      cards.append({
        "position": position,
        "is_open": is_open,
        "value": value,
        "board_id": board_id,
      }.copy())
  print(cards)
  return cards
