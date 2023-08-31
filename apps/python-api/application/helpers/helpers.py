from datetime import datetime, timedelta
from jose import jwt

async def create_access_token(
    data: dict,
    access_token_expire_minutes: int,
    secret_key: str,
    algorithm: str
    ):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=access_token_expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt
