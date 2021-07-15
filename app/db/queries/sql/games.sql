-- name: get_game_info_by_board_id^
SELECT id,
       board_id,
       click_count,
       is_finish,
       columns,
       rows
FROM games
WHERE board_id = :board_id
LIMIT 1;

-- name: create-new-game<!
INSERT INTO games (board_id, click_count, is_finish, columns, rows)
VALUES (:board_id, :click_count, :is_finish, :columns, :rows)
RETURNING
    id, created_at, updated_at;

-- name: update_game_click_count
UPDATE games
SET click_count = :click_count
WHERE board_id = :board_id
RETURNING
    id, created_at, updated_at;

