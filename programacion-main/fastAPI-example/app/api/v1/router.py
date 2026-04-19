from fastapi import APIRouter
from app.api.v1.endpoints.artists import router as artists_router
from app.api.v1.endpoints.albums import router as albums_router

api_router = APIRouter()
api_router.include_router(artists_router, prefix="/artists", tags=["artists"])
api_router.include_router(albums_router, prefix="/albums", tags=["albums"])