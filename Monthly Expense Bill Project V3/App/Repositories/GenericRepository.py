from .IGenericRepository import IGenericRepository
from App.database import Session
from typing import TypeVar, List

Entity = TypeVar('Entity')

class GenericRepository(IGenericRepository):
    def __init__(self, db: Session, modelType: type(Entity)):
        self.db = db
        self.modelType = modelType
        #self.schema 
        
    def save(self, data: Entity) ->Entity:
        self.db.add(data)
        self.db.commit()
        self.db.refresh(data)
        return data
    
    def getByID(self, id: str) -> Entity:
        pass
    
    def getByID(self, id: str) -> List[Entity]:
        pass 
    
    def getAll(self) -> list[Entity]:
        data = self.db.query(self.modelType).all()
        for i in data:
            print(i.ID, i.username, i.passward)
        return "Showed"
    
    def update(self, entity:Entity) -> Entity:
        pass
    
    def delete(self, entity:Entity) -> None:
        pass
    
    def delete(self, id:int) -> None:
        pass    