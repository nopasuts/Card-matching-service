from fastapi import APIRouter

from app.api.routes import games, cards

router = APIRouter()
router.include_router(games.router, tags=["games"], prefix="/games")
router.include_router(cards.router, tags=["cards"], prefix="/cards")
