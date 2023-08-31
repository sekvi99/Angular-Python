from pydantic import BaseModel
from typing import Optional

class UserResponse(BaseModel):
    
    message: str
    username: Optional[str]
    email: Optional[str]
    
    
    class Config:
        orm_mode = True