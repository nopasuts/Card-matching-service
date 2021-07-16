from fastapi import APIRouter

from app.api.routes import games, cards, stats

router = APIRouter()
router.include_router(games.router, tags=["games"], prefix="/games")
router.include_router(cards.router, tags=["cards"], prefix="/cards")
router.include_router(stats.router, tags=["stats"], prefix="/stats")
