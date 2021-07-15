from typing import List

def get_card_rows(game_id: int, column: int, row: int, shuffleArrayNumber: List[int]):
  order = 0
  cards = []
  for eachCol in range(column):
    for eachRow in range(row):
      position = "{0}x{1}".format(eachCol+1, eachRow+1)
      is_open = False
      value = shuffleArrayNumber[order]
      order += 1
      cards.append({
        "position": position,
        "is_open": is_open,
        "game_id": game_id,
        "value": value,
      }.copy())
  return cards

def is_cards_match(first_card, second_card):
  if first_card["value"] == second_card["value"]:
    return True
  return False
