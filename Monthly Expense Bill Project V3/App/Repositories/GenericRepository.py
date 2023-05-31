from .IGenericRepository import IGenericRepository
from App.database import session, Base
from typing import TypeVar, List
#from App.Models.BaseModel import Schema
from App.Models.User import User

Entity = TypeVar('Entity', bound = Base)

class GenericRepository(IGenericRepository):
    def __init__(self, modelType: type(Entity)):
        #self.db = db
        self.modelType = modelType
        #self.schema = schema
        
    def save(self, data: Entity) ->Entity:
        session.add(data)
        session.commit()
        session.refresh(data)
        return data
    
    ### Used to do delete. Only returthe ID but not in json formate 
    def getByIDFirst(self, id: int) -> Entity:
        return session.query(self.modelType).filter_by(ID = id).first()
    
    def getByID(self, id: str) -> List[Entity]:
       #data= session.query(self.modelType).filter_by(ID=id).first()
       return session.query(self.modelType).filter_by(ID=id).first() 
    
    def getAll(self) -> List[Entity]:
        return session.query(self.modelType).all()
    
    def update(self,  userUpdate : User) -> Entity:
        data = session.query(self.modelType).filter_by(ID = userUpdate.ID).first()
        data.password = userUpdate.password
        session.commit()
        session.refresh(data)

    
    # def delete(self, entity:Entity) -> None:
    #     self.db.delete(entity)
    #     self.db.commit()
    
    def deleteData(self, id:int) -> None:
        session.query(self.modelType).filter_by(ID = id).delete()
        session.commit()    