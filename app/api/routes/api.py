from fastapi import APIRouter

from app.api.routes import games

router = APIRouter()
router.include_router(games.router, tags=["games"], prefix="/games")
