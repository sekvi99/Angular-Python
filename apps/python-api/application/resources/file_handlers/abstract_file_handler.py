import logging
import os
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict


@dataclass
class FileHandler(ABC):
    """
    Class that definies way of handling files with diffrent extensions used in application.
    """
    
    _file_path: str # Private variable for storing information of file path to given file
    
    def __post_init__(self) -> None:
        """
        Post init method for checking whether provided path exist in OS.
        """
        if not os.path.exists(self._file_path):
            logging.error(f'Path to file does not exist: {self._file_path} in OS.')
        
    @property
    def file_path(self) -> str:
        """
        Getter for extracting information about file path.

        Returns:
            str: String representation of file path to given file.
        """
        return self._file_path
    
    @file_path.setter
    def file_path(self, path: str) -> None:
        """
        Setter for setting file path to given file.

        Args:
            path (str): String representation of path  to file.

        Raises:
            FileNotFoundError: Occures when file does not exist under provided path.
        """
        if os.path.exists(path):
            self._file_path = path
        else:
            msg = f'File {path} does not exist.'
            logging.error(msg)
            raise FileNotFoundError(msg)
        
    @abstractmethod
    def read(self):
        """
        Definition of method 'read' to implement in derivative classes.
        
        Should:
            Method should allow to read whole content of file provided under _file_path property. 
        """
        ...
        
    @abstractmethod
    def write(self, data: Dict[str, str]):
        """
        Definition of method 'write' to implement in derivative classes.
        
        Args:
            data (Dict[str, str]): Dictionary representation of data to save in given file in format key: value.
        
        Should:
            Method should allow to write data provided in dictionary format to file set up under _file_path property.
        """
        ...