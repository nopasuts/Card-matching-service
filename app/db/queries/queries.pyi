"""Typings for queries generated by aiosql"""

from typing import Dict, Optional, Sequence

from asyncpg import Connection, Record

class TagsQueriesMixin:
    async def get_all_tags(self, conn: Connection) -> Record: ...
    async def create_new_tags(
        self, conn: Connection, tags: Sequence[Dict[str, str]]
    ) -> None: ...

class UsersQueriesMixin:
    async def get_user_by_email(self, conn: Connection, *, email: str) -> Record: ...
    async def get_user_by_username(
        self, conn: Connection, *, username: str
    ) -> Record: ...
    async def create_new_user(
        self,
        conn: Connection,
        *,
        username: str,
        email: str,
        salt: str,
        hashed_password: str
    ) -> Record: ...
    async def update_user_by_username(
        self,
        conn: Connection,
        *,
        username: str,
        new_username: str,
        new_email: str,
        new_salt: str,
        new_password: str,
        new_bio: Optional[str],
        new_image: Optional[str]
    ) -> Record: ...

class ProfilesQueriesMixin:
    async def is_user_following_for_another(
        self, conn: Connection, *, follower_username: str, following_username: str
    ) -> Record: ...
    async def subscribe_user_to_another(
        self, conn: Connection, *, follower_username: str, following_username: str
    ) -> None: ...
    async def unsubscribe_user_from_another(
        self, conn: Connection, *, follower_username: str, following_username: str
    ) -> None: ...

class CommentsQueriesMixin:
    async def get_comments_for_article_by_slug(
        self, conn: Connection, *, slug: str
    ) -> Record: ...
    async def get_comment_by_id_and_slug(
        self, conn: Connection, *, comment_id: int, article_slug: str
    ) -> Record: ...
    async def create_new_comment(
        self, conn: Connection, *, body: str, article_slug: str, author_username: str
    ) -> Record: ...
    async def delete_comment_by_id(
        self, conn: Connection, *, comment_id: int, author_username: str
    ) -> None: ...

class ArticlesQueriesMixin:
    async def add_article_to_favorites(
        self, conn: Connection, *, username: str, slug: str
    ) -> None: ...
    async def remove_article_from_favorites(
        self, conn: Connection, *, username: str, slug: str
    ) -> None: ...
    async def is_article_in_favorites(
        self, conn: Connection, *, username: str, slug: str
    ) -> Record: ...
    async def get_favorites_count_for_article(
        self, conn: Connection, *, slug: str
    ) -> Record: ...
    async def get_tags_for_article_by_slug(
        self, conn: Connection, *, slug: str
    ) -> Record: ...
    async def get_article_by_slug(self, conn: Connection, *, slug: str) -> Record: ...
    async def create_new_article(
        self,
        conn: Connection,
        *,
        slug: str,
        title: str,
        description: str,
        body: str,
        author_username: str
    ) -> Record: ...
    async def add_tags_to_article(
        self, conn: Connection, tags_slugs: Sequence[Dict[str, str]]
    ) -> None: ...
    async def update_article(
        self,
        conn: Connection,
        *,
        slug: str,
        author_username: str,
        new_slug: str,
        new_title: str,
        new_body: str,
        new_description: str
    ) -> Record: ...
    async def delete_article(
        self, conn: Connection, *, slug: str, author_username: str
    ) -> None: ...
    async def get_articles_for_feed(
        self, conn: Connection, *, follower_username: str, limit: int, offset: int
    ) -> Record: ...

class GamesQueriesMixin:
    async def get_game_info_by_board_id(self, conn: Connection, *, board_id: str) -> Record: ...
    async def create_new_game(
        self, conn: Connection, board_id: str, click_count: int, is_finish
    ) -> Record: ...
    async def update_game_by_board_id(
        self,
        conn: Connection,
        *,
        board_id: str,
        click_count: int,
    ) -> Record: ...

class Queries(
    TagsQueriesMixin,
    UsersQueriesMixin,
    ProfilesQueriesMixin,
    CommentsQueriesMixin,
    ArticlesQueriesMixin,
    GamesQueriesMixin,
): ...

queries: Queries
