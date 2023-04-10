from Models.Context import Session
from Models.ExpenseLocation import ExpenseLocation
from .IService import IService
from Repositories.ExpenseLocationRepository import ExpenseLocationRepository
from typing import List 

class ExpenseLocationServie(IService):
    
    def __init__(self, db: Session):
        self.db =  db
        self.repo = ExpenseLocationRepository(db)
        
    def getAll(self) -> List[ExpenseLocation]:
        return self.repo.getAll()
    
    def getByID(self, id: str):
        return self.repo.getByID(id)
    
    def save(self, newExpenseLocation: ExpenseLocation) -> ExpenseLocation:
        if (len(newExpenseLocation).ID==0 or newExpenseLocation == " "):
            raise ValueError("Invalid Expense Head ID")
        
        return self.repo.save(newExpenseLocation)
        
    
    def update(self, ExpenseLocationUpdate: ExpenseLocation):
        expenseLocation = self.repo.getByID(ExpenseLocationUpdate.ID)
        expenseLocation.ShortName = ExpenseLocationUpdate.ShortName
        
        return self.repo.update(expenseLocation)

    
    def delete(self, ID: str):
        expenseLocation = self.repo.getByID(ID)
        if(expenseLocation == None):
            raise ValueError(f'Expense Location is not found with ID:{ID}')
        
        return self.repo.delete(expenseLocation)