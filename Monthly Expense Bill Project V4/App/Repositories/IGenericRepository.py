from abc import ABC, abstractmethod
from typing import List, TypeVar
from ..database import Base


T = TypeVar('T', bound=Base)

class IGenericRepository(ABC):
    
    
    @abstractmethod
    def save(self):
        pass
    
    @abstractmethod
    def getAll(self) -> List[T]:
        pass
    
    @abstractmethod
    def getByID(self) -> T:
        pass
    
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def deleteData(self):
        pass 