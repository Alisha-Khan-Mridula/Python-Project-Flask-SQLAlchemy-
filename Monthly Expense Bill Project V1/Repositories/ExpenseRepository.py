from Models.Expense import Expense, ExpenseSchema
from Models.Context import Session
from .GenericRepository import GenericRepository

class ExpenseRepository(GenericRepository):
    def __init__(self, db: Session):
        super().__init__(db, Expense, ExpenseSchema() )