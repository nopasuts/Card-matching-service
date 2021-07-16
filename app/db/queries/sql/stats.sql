
-- name: get_user_by_user_id^
SELECT id,
       user_id,
       best_click_count
FROM stats
WHERE user_id = :user_id
LIMIT 1;

-- name: create_new_user<!
INSERT INTO stats (user_id, best_click_count)
VALUES (:user_id, :best_click_count)
RETURNING
    id,user_id, best_click_count, created_at, updated_at;

-- name: update_user_best_click_count<!
UPDATE stats
SET best_click_count = :best_click_count
WHERE user_id = :user_id
RETURNING
    id, best_click_count, created_at, updated_at;

-- name: update_global_best_click_count<!
UPDATE stats
SET best_click_count = :best_click_count
WHERE user_id = 'GLOBAL_STAT'
RETURNING
    id, best_click_count, created_at, updated_at;