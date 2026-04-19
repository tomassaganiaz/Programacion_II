from pydantic import BaseModel
from typing import Optional

class AlbumBase(BaseModel):
    Title: str
    ArtistId: int

class AlbumCreate(AlbumBase):
    pass

class AlbumUpdate(BaseModel):
    Title: Optional[str] = None
    ArtistId: Optional[int] = None

class Album(AlbumBase):
    AlbumId: int

    class Config:
        from_attributes = True