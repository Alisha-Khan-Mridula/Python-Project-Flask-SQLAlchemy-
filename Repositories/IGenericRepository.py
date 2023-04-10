#This file holdes the abstract class and methods pf Generic repository class methods 

from typing import TypeVar, List
from abc import ABC, abstractmethod
from Models.Context import Base  

Entity = TypeVar('Entity', bound = Base)

class IGenericRepository(ABC):
    
    @abstractmethod
    def getByID(self, id:int) -> Entity:
        pass

    @abstractmethod
    def getByID(self, id: str) -> Entity:
        pass

    @abstractmethod
    def getAll(self) -> List[Entity]:
        pass

    @abstractmethod
    def save(self, entity:Entity) -> Entity:
        pass

    @abstractmethod
    def update(self, enitity:Entity) -> Entity:
        pass

    @abstractmethod
    def delete(self, entity:Entity) -> None:
        pass

    @abstractmethod
    def delete(self, id:int) -> None:
        pass 