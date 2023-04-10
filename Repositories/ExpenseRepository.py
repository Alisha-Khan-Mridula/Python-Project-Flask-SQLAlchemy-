from Models.Expense import Expense
from Models.Context import Session
from .GenericRepository import GenericRepository

class ExpenseRepository(GenericRepository):
    def __init__(self, db: Session) -> None:
        super().__init__(db, Expense )