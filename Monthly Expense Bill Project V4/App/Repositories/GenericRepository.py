from App.Repositories.IGenericRepository import IGenericRepository
from App.database import session, Base
from App.Models.User import Schema
from typing import TypeVar, List

T = TypeVar('T', bound = Base)

class GenericRepositort():
    
    def __init__(self, modeltype:type(T)):
       self.modeltype = modeltype
        
    def save(self, entity : T):
        session.add(entity)
        session.commit()
        session.refresh(entity)
        return entity
    
    def getAll(self) -> List[T]:
        return session.query(self.modeltype).all()
    
    
    def getByID():
        pass
    
    def deleteData():
        pass
    
    def update():
        pass