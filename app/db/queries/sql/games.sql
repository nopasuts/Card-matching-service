-- name: get_game_info_by_game_id^
SELECT id,
       board_id,
       click_count,
       is_finish,
       created_at,
       updated_at
FROM games
WHERE board_id = :board_id
LIMIT 1;

-- name: create-new-game<!
INSERT INTO games (board_id, click_count, is_finish)
VALUES (:board_id, :click_count, :is_finish)
RETURNING
    id, created_at, updated_at;

