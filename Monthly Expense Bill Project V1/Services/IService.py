from abc import ABC, abstractmethod

class IService(ABC):
    
    @abstractmethod
    def getAll(self):
        pass
    
    @abstractmethod
    def getByID(self):
        pass
    
    @abstractmethod
    def save(self):
        pass
    
    @abstractmethod
    def update(self):
        pass 
    
    @abstractmethod
    def delete(self):
        pass