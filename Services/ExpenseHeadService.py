from Models.Context import Session
from Models.ExpenseHead import ExpenseHead
from .IService import IService
from Repositories.ExpenseHeadRepository import ExpenseHeadRepository
from typing import List

class ExpenseHeadServie(IService):
    
    def __init__(self, db: Session):
        self.db =  db
        self.repo = ExpenseHeadRepository(db)
        
    def getAll(self) -> List[ExpenseHead]:
        return self.repo.getAll()
    
    def getByID(self, id: str):
        return self.repo.getByID(id)
    
    def save(self, newExpenseHead: ExpenseHead) -> ExpenseHead:
        # if (len(newExpenseHead).ID==0 or newExpenseHead == " "):
        #     raise ValueError("Invalid Expense Head ID")
        
        return self.repo.save(newExpenseHead)
        
    
    def update(self, ExpenseHeadUpdate: ExpenseHead):
        expenseHead = self.repo.getByID(ExpenseHeadUpdate.ID)
        expenseHead.HeadName = ExpenseHeadUpdate.HeadName
        #expenseHead.CreatedByID = ExpenseHeadUpdate.CreatedByID
        #expenseHead.UpdatedByID = ExpenseHeadUpdate.UpdatedByID
        
        return self.repo.update(expenseHead)

    
    def delete(self, ID: str):
        expenseHead = self.repo.getByID(ID)
        if(expenseHead == None):
            raise ValueError(f'Expense Head is not found with ID:{ID}')
        
        return self.repo.delete(expenseHead)
         
        