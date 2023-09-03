from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class ExternalResourceApiHandler(ABC):
    
    url: str # Api url to hit
    api_key: str # String representation of api key
    obtained_data: dict = field(init=False) # Obtained data set after get_api_response method
    
    @abstractmethod
    def get_api_response(self) -> int:
        """
        Method should hit desired endpoint passed as url prop.
        Whether request was successfull it should save data to obtained_data prop.
        
        Returns:
            int: Response status code.
        """
        ...
        
    @abstractmethod
    def transform_api_response_to_desired_format(self) -> dict:
        """
        Method should transform obtained data field do desired format.

        Returns:
            dict[any]: Desired representation of data obtained from api.
        """
        ...