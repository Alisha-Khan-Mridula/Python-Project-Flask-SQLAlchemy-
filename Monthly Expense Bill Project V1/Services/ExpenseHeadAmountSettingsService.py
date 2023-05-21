from Models.Context import Session
from Models.ExpenseHeadAmountSettings import ExpenseHeadAmountSettings
from .IService import IService
from Repositories.ExpenseHeadAmountSettingsRepository import ExpenseHeadAmountSettingsRepository
from typing import List 

class ExpenseHeadAmountSettingsServie(IService):
    
    def __init__(self, db: Session):
        self.db =  db
        self.repo = ExpenseHeadAmountSettingsRepository(db)
        
    def getAll(self) -> List[ExpenseHeadAmountSettings]:
        return self.repo.getAll()
    
    def getByID(self, id: str):
        return self.repo.getByID(id)
    
    def save(self, newExpenseHeadAmount: ExpenseHeadAmountSettings) -> ExpenseHeadAmountSettings:
        #if (len(newExpenseHeadAmount).ID==0 or newExpenseHeadAmount == " "):
         #   raise ValueError("Invalid Expense Expense Head Amount Settings ID")
        
        return self.repo.save(newExpenseHeadAmount)
        
    
    def update(self, ExpenseHeadAmountUpdate: ExpenseHeadAmountSettings):
        expenseAmount = self.repo.getByID(ExpenseHeadAmountUpdate.ID)
        expenseAmount.Designation = ExpenseHeadAmountUpdate.Designation
        #expenseAmount.Amount = ExpenseHeadAmountUpdate.Amount
        #print(expenseAmount.Amount)
        #print(ExpenseHeadAmountUpdate.Amount)
        
        return self.repo.update(expenseAmount)

    
    def delete(self, ID: str):
        expenseAmount = self.repo.getByID(ID)
        if(expenseAmount == None):
            raise ValueError(f'Expense Head Amount is not found with ID:{ID}')
        
        return self.repo.delete(expenseAmount)