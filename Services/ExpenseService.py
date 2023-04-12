from Models.Context import Session
from Models.Expense import Expense
from Repositories.ExpenseRepository import ExpenseRepository
from .IService import IService
from typing import List


class ExpenseService(IService):
    def __init__(self, db: Session):
        self.db = db
        self.repo = ExpenseRepository(db)
        
    def getAll(self) -> List[Expense]:
        return self.repo.getAll()
    
    def getByID(self, id: int):
        return self.repo.getByID(id)
    
    def save(self, newExpense: Expense) -> Expense:
        # if (len(newExpense).ID==0 or newExpense == " "):
        #     raise ValueError("Invalid Expense Head ID")
        
        return self.repo.save(newExpense)
        
    
    def update(self, ExpenseUpdate: Expense):
        expense = self.repo.getByID(ExpenseUpdate.ID)
        expense.EmployeeID = ExpenseUpdate.EmployeeID
        expense.ExpenseMonth = ExpenseUpdate.ExpenseMonth
        
        return self.repo.update(expense)
        

    
    def delete(self, ID: int):
        expense = self.repo.getByID(ID)
        if(expense == None):
            raise ValueError(f'Expense is not found with ID:{ID}')
        
        return self.repo.delete(expense)