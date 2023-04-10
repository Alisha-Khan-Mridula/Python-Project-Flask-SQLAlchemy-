from Models.ExpenseDetails import ExpenseDetails
from Models.Context import Session
from .GenericRepository import GenericRepository

class ExpenseDetailsRepository(GenericRepository):
    def __init__(self, db: Session) -> None:
        super().__init__(db, ExpenseDetails)
        
