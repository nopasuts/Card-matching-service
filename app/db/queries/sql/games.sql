-- name: get_game_info_by_game_id^
SELECT id,
       game_id,
       click_count,
       is_finish,
       created_at,
       updated_at
FROM games
WHERE game_id = :game_id
LIMIT 1;
