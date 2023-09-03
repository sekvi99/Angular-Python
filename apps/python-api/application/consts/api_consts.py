from typing import Final

from application.consts.consts import API_ENV_FILE, ENV_HANDLER
from application.resources.file_handlers.env_handler.env_handler import \
    EnvFileHandler

API_KEY_NAME: Final[str] = ENV_HANDLER.read_var_by_name('API_KEY_NAME') # Extracting api key name from .env file
API_KEY: Final[str] = ENV_HANDLER.read_var_by_name('API_KEY') # Extracting api key from .env file

# Obtain yt api key
YT_ENV_HANDLER: Final[EnvFileHandler] = EnvFileHandler(API_ENV_FILE)    
YT_API_KEY: Final[str] = YT_ENV_HANDLER.read_var_by_name('YT_API_KEY') # Extracting key for accessing yt stats
