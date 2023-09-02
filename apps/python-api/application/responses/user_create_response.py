from typing import Optional

from pydantic import BaseModel


class UserCreateRequest(BaseModel):
    username: str
    email: str
    password: str
    connected_mail: Optional[str]