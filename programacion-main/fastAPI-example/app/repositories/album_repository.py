from sqlalchemy import select
from app.repositories.base_repository import BaseRepository
from app.models.album import Album
from app.schemas.album import AlbumCreate, AlbumUpdate

class AlbumRepository(BaseRepository[Album, AlbumCreate, AlbumUpdate]):
    """Album-specific repository."""

    async def get_by_title(self, db, title: str):
        """Get album by title."""
        result = await db.execute(
            select(Album).where(Album.Title == title)
        )
        return result.scalars().first()

    async def get_by_artist(self, db, artist_id: int):
        """Get albums by artist ID."""
        result = await db.execute(
            select(Album).where(Album.ArtistId == artist_id)
        )
        return result.scalars().all()

album_repository = AlbumRepository(Album)