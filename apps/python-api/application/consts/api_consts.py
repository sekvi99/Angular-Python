from typing import Final

from application.consts.consts import ENV_HANDLER

API_KEY_NAME: Final[str] = ENV_HANDLER.read_var_by_name('API_KEY_NAME') # Extracting api key name from .env file
API_KEY: Final[str] = ENV_HANDLER.read_var_by_name('API_KEY') # Extracting api key from .env file