from .IGenericRepository import IGenericRepository
from App.database import Session
from typing import TypeVar, List
from App.Models.BaseModel import Schema
from App.Models.User import User

Entity = TypeVar('Entity')

class GenericRepository(IGenericRepository):
    def __init__(self, db: Session, modelType: type(Entity), schema: Schema):
        self.db = db
        self.modelType = modelType
        self.schema = schema
        
    def save(self, data: Entity) ->Entity:
        self.db.add(data)
        self.db.commit()
        self.db.refresh(data)
        return data
    
    ### Used to do delete. Only returthe ID but not in json formate 
    def getByIDFirst(self, id: int) -> Entity:
        return self.db.query(self.modelType).filter_by(ID = id).first()
    
    def getByID(self, id: str) -> List[Entity]:
       data= self.db.query(self.modelType).filter_by(ID=id).first()
       return self.schema.dump(data) 
    
    def getAll(self) -> List[Entity]:
        data = self.db.query(self.modelType).all()
        # for i in data:
        #     print(i.ID, i.username, i.passward)
        return [self.schema.load(self.schema.dump(item)) for item in data]
    
    def update(self,  userUpdate : User) -> Entity:
        data = self.db.query(self.modelType).filter_by(ID = userUpdate.ID).first()
        data.password = userUpdate.password
        self.db.commit()
        self.db.refresh(data)

    
    # def delete(self, entity:Entity) -> None:
    #     self.db.delete(entity)
    #     self.db.commit()
    
    def deleteData(self, id:int) -> None:
        self.db.query(self.modelType).filter_by(ID = id).delete()
        self.db.commit()    