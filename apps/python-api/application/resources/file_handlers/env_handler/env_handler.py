import logging
from dataclasses import dataclass
from typing import Dict

from application.resources.file_handlers.abstract_file_handler import \
    FileHandler
from dotenv import dotenv_values


@dataclass
class EnvFileHandler(FileHandler):
    """
    Class that definies way of extracting/ setting data in .env files.

    Args:
        FileHandler (_type_): Inheritence of FileHandler class.
    """
    
    def read(self) -> Dict[str, str]:
        """
        Implementation of abstract method. Method allows to read whole content of .env file.

        Returns:
            Dict[str, str]: Dictionary representation of .env file data.
        """
        env_data = {}
        with open(self._file_path, 'r') as f:
            for line in f:
                k, v = line.split('=', 1)
                env_data[k] = v
                
        logging.info(f'Correctly extracted info from .env file: {self._file_path}')
        return env_data
    
    def read_var_by_name(self, var_name: str) -> str:
        """
        Method for extracting value of given variable by its name.

        Args:
            var_name (str): String representation of .env variable name.

        Returns:
            str: String representation of .env variable value.
        """
        env_variables = dotenv_values(self._file_path)
        val = env_variables.get(var_name)
        
        if val:
            logging.info(f'Correctly extracted: {var_name} from .env file.')
            return val
        
        else:
            logging.error(f'Unable to extract {var_name} from .env file')
    
    def write(self, data: Dict[str, str]) -> None:
        """
        Implementation of abstract method. Method allows to save data to .env file.

        Args:
            data (Dict[str, str]): _description_
            
        Raises:
            TypeError: Occures when provided data is in unexpected type.
        """
        
        if isinstance(data, dict):
            with open(self._file_path, 'w') as f:
                for k, v in data.items():
                    f.write(f'{k}={v}')

            logging.info('Correctly saved data to .env file')
            
        else:
            logging.error('Unable to save data to .env file')
            raise TypeError(f'Expected dictionary provided: {type(data)}')