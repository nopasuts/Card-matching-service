-- name: create-new-card<!
INSERT INTO cards (board_id, click_count, is_finish)
VALUES (:board_id, :click_count, :is_finish)
RETURNING
    id, created_at, updated_at;
