#Common functions of all the models 

from typing import TypeVar, List
from Models.Context import Session, Base, Schema
from .IGenericRepository import IGenericRepository

Entity = TypeVar('Entity')


class GenericRepository(IGenericRepository):
    def __init__(self, db: Session, modelType: type(Entity), schema: Schema):
        self.db = db
        self.modelType = modelType
        self.schema = schema  
        
        
    # def getByID(self, ID: int):
    #     data= self.db.query(self.modelType).filter_by(ID=ID).first()
    #     return self.schema.dump(data)

    
    def getByID(self, ID: str):
       data= self.db.query(self.modelType).filter_by(ID=ID).first()
       return self.schema.dump(data)
    
    def getAll(self) ->List[Entity]:
        data = self.db.query(self.modelType).all()
        return [self.schema.load(self.schema.dump(item)) for item in data]
    
    def save(self, data: Entity) -> Entity:
        self.db.add(data)
        self.db.commit()
        self.db.refresh(data)
        return data
    
    def update(self, entity:Entity) -> Entity:
        self.db.commit()    
        self.db.refresh(entity)
        return entity


        
    def delete(self,ID: int):
        self.db.query(self.modelType).filter(ID = ID).delete()
        self.db.commit()
  
    def delete(self,entity: Entity):
        self.db.delete(entity)
        self.db.commit()
            
        
    