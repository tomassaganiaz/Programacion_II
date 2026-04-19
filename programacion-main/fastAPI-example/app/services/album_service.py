from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException
from app.repositories.album_repository import album_repository
from app.repositories.artist_repository import artist_repository
from app.schemas.album import AlbumCreate, AlbumUpdate, Album

class AlbumService:
    """Business logic for albums."""

    def __init__(self):
        self.repository = album_repository

    async def get_album(self, db: AsyncSession, album_id: int) -> Optional[Album]:
        """Get album by ID."""
        return await self.repository.get(db, album_id)

    async def get_albums(self, db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Album]:
        """Get multiple albums."""
        return await self.repository.get_multi(db, skip, limit)

    async def create_album(self, db: AsyncSession, album_in: AlbumCreate) -> Album:
        """Create new album."""
        # Validate that artist exists
        artist = await artist_repository.get(db, album_in.ArtistId)
        if not artist:
            raise HTTPException(status_code=400, detail="Artist not found")
        return await self.repository.create(db, album_in)

    async def update_album(self, db: AsyncSession, album_id: int, album_in: AlbumUpdate) -> Optional[Album]:
        """Update album."""
        album = await self.repository.get(db, album_id)
        if not album:
            return None
        
        # Validate artist if provided
        if album_in.ArtistId is not None:
            artist = await artist_repository.get(db, album_in.ArtistId)
            if not artist:
                raise HTTPException(status_code=400, detail="Artist not found")
        
        return await self.repository.update(db, album, album_in)

    async def delete_album(self, db: AsyncSession, album_id: int) -> bool:
        """Delete album."""
        return await self.repository.delete(db, album_id)

    async def get_albums_by_artist(self, db: AsyncSession, artist_id: int) -> List[Album]:
        """Get albums by artist ID."""
        # Validate that artist exists
        artist = await artist_repository.get(db, artist_id)
        if not artist:
            raise HTTPException(status_code=404, detail="Artist not found")
        return await self.repository.get_by_artist(db, artist_id)

album_service = AlbumService()