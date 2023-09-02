from fastapi import Depends, HTTPException
from fastapi.security.api_key import APIKeyHeader

from application.consts.api_consts import API_KEY, API_KEY_NAME

api_key_header = APIKeyHeader(name=API_KEY_NAME)

def authorize(api_key: str = Depends(api_key_header)) -> bool:
    """
    Helper function for checking whether api authorization was successfull.
    
    Args:
        api_key (str): Provided api-key.
        
    Return:
        bool: True if authentication was successfull.
        
    Raises:
        HttpException: Occures when endpoint with wrong api key or without it has been hit.
    """    
    if api_key == API_KEY:
        return True
    
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")