from datetime import datetime, timedelta

from fastapi import Depends, HTTPException
from jose import JWTError, jwt

from application.consts.consts import ALGORITHM, SECRET_KEY


# https://console.cloud.google.com/apis/api/youtube.googleapis.com/metrics?project=youtube-stats-397911&hl=pl&supportedpurview=project
def is_token_valid(token: str) -> bool:
    """
    Helper function for checking whether generated JWT token is valid. 

    Args:
        token (str): String representation of the user's JWT token.

    Returns:
        bool: True/False based on whether the token is valid or expired.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Check the expiration time
        expiration_time = datetime.fromtimestamp(payload["exp"])
        current_time = datetime.utcnow()
        if current_time < expiration_time:
            return True
        else:
            return False
    except JWTError:
        return False
    

def get_current_user(token: str = Depends(is_token_valid)):
    """
    Helper function for accessing and checking whether user token is valid

    Args:
        token (str, optional): User token. Defaults to Depends(is_token_valid).

    Raises:
        HTTPException: Occures when token is invalid or has exipred.

    Returns:
        str: String representation of token.
    """
    if not token:
        raise HTTPException(status_code=401, detail='Token is invalid or has expired')
    return token