from typing import TypeVar, List
from abc import ABC, abstractmethod
from App.database import Base

Entity = TypeVar('Entity', bound = Base)

class IGenericRepository(ABC):
    
    @abstractmethod
    def save(self, entity:Entity) -> Entity:
        pass
    
    @abstractmethod
    def getByID(self, id: str) -> Entity:
        pass
    
    @abstractmethod
    def getByID(self, id: str) -> List[Entity]:
        pass 
    
    @abstractmethod
    def getAll(self) -> list[Entity]:
        pass
    
    @abstractmethod
    def update(self, entity:Entity) -> Entity:
        pass
    
    # @abstractmethod
    # def delete(self, entity:Entity) -> None:
    #     pass
    
    @abstractmethod
    def deleteData(self, id:int) -> None:
        pass