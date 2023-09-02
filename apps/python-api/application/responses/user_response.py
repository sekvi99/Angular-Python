from typing import Optional

from pydantic import BaseModel


class UserResponse(BaseModel):
    
    message: str
    username: Optional[str]
    email: Optional[str]
    
    
    class Config:
        orm_mode = True