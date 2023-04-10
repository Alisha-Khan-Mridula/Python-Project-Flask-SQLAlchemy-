from Models.Context import Session
from Models.ExpenseDetails import ExpenseDetails
from .IService import IService
from Repositories.ExpenseDetailsRepository import ExpenseDetailsRepository
from typing import List 

class ExpenseDetailsServie(IService):
    
    def __init__(self, db: Session):
        self.db =  db
        self.repo = ExpenseDetailsRepository(db)
        
    def getAll(self) -> List[ExpenseDetails]:
        return self.repo.getAll()
    
    def getByID(self, id: str):
        return self.repo.getByID(id)
    
    def save(self, newExpenseDetails: ExpenseDetails) -> ExpenseDetails:
        if (len(newExpenseDetails).ID==0 or newExpenseDetails == " "):
            raise ValueError("Invalid Expense Details ID")
        
        return self.repo.save(newExpenseDetails)
        
    
    def update(self, ExpenseDetailsUpdate: ExpenseDetails):
        expenseDetails = self.repo.getByID(ExpenseDetailsUpdate.ID)
        expenseDetails.locationFrom = ExpenseDetailsUpdate.LocationFrom
        
        return self.repo.update(expenseDetails)

    
    def delete(self, ID: str):
        expenseDetails = self.repo.getByID(ID)
        if(expenseDetails == None):
            raise ValueError(f'Expense Details is not found with ID:{ID}')
        
        return self.repo.delete(expenseDetails)