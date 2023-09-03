from pydantic import BaseModel

class YouTubeRequestModel(BaseModel):
    url: str

class YouTubeStatsResponse(BaseModel):
    
    views: int
    likes: int
    favourites: int
    comments: int