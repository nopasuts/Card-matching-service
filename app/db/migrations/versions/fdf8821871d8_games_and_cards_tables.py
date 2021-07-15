"""games and cards table

Revision ID: fdf8821871d8
Revises:
Create Date: 2021-07-15 01:36:44.791880

"""
from typing import Tuple

import sqlalchemy as sa
from alembic import op
from sqlalchemy import func

revision = "fdf8821871d8"
down_revision = None
branch_labels = None
depends_on = None


def create_updated_at_trigger() -> None:
    op.execute(
        """
    CREATE FUNCTION update_updated_at_column()
        RETURNS TRIGGER AS
    $$
    BEGIN
        NEW.updated_at = now();
        RETURN NEW;
    END;
    $$ language 'plpgsql';
    """
    )


def timestamps() -> Tuple[sa.Column, sa.Column]:
    return (
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=func.now(),
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=func.now(),
        ),
    )


def create_games_table() -> None:
    op.create_table(
        "games",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("game_id", sa.Text, unique=True, nullable=False, index=True),
        sa.Column("click_count", sa.Integer, nullable=False),
        sa.Column("is_finish", sa.Boolean, nullable=False),
        *timestamps(),
    )
    op.execute(
        """
        CREATE TRIGGER update_game_modtime
            BEFORE UPDATE
            ON games
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


def create_cards_table() -> None:
    op.create_table(
        "cards",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("position", sa.Text, nullable=False, index=True),
        sa.Column("is_open", sa.Boolean, nullable=False),
        sa.Column("value", sa.Integer, nullable=False),
        sa.Column(
            "game_id", sa.Text, sa.ForeignKey("games.game_id", ondelete="SET NULL")
        ),
        *timestamps(),
    )
    op.execute(
        """
        CREATE TRIGGER update_card_modtime
            BEFORE UPDATE
            ON cards
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


def upgrade() -> None:
    create_updated_at_trigger()
    create_cards_table()
    create_games_table()


def downgrade() -> None:
    op.drop_table("games")
    op.drop_table("cards")
    op.execute("DROP FUNCTION update_updated_at_column")
