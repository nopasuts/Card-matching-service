-- name: get_cards_by_game_id
SELECT id,
       position,
       is_open
FROM cards
WHERE game_id = :game_id

-- name: get_card_by_position^
SELECT id,
       value,
       is_open
FROM cards
WHERE position = :position AND game_id = :game_id
LIMIT 1;

-- name: create-new-cards*!
INSERT INTO cards (position, is_open, game_id, value)
VALUES (:position, :is_open, :game_id, :value)

-- name: update_is_open_card!
UPDATE cards
SET is_open = :is_open
WHERE game_id = :game_id AND position = :position
