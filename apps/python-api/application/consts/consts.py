from application.resources.file_handlers.env_handler.env_handler import EnvFileHandler
import os
from typing import Final

"""Set Absoulte Path"""
APP_DIR: Final[str] = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Path to application directory
ENV_FILE: Final[str] = os.path.join(APP_DIR, r'resources/files/env/.env')         # Path to .env file

""".ENV File consts"""
ENV_HANDLER: Final[EnvFileHandler] = EnvFileHandler(ENV_FILE)                      # Creating .env obj reader
DB_USER: Final[str] = ENV_HANDLER.read_var_by_name('DB_USER')                      # Extracting db user name for database
DB_PASSWORD: Final[str] = ENV_HANDLER.read_var_by_name('DB_PASSWORD')              # Extracting password for database user
DB_DATABASE: Final[str] = ENV_HANDLER.read_var_by_name('DB_DATABASE')              # Extracting database name
DB_PORT: Final[str] = ENV_HANDLER.read_var_by_name('DB_PORT')                      # Extracting port for database
DB_PROVIDER: Final[str] = os.getenv('PROD_URL') if os.getenv('PROD_URL') is not None else 'localhost'
DB_POSTGRES_URL: Final[str] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_PROVIDER}:{DB_PORT}/{DB_DATABASE}' # Url for connecting with postgres
