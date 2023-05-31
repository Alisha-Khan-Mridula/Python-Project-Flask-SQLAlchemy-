from abc import ABC, abstractmethod
from typing import TypeVar
from App.database import Base



Entity = TypeVar('Entity', bound=Base)

class IGenericRepository(ABC):
    
    @abstractmethod
    def save(self) -> Entity:
        pass
    
    @abstractmethod
    def getByID(self) -> Entity:
        pass 