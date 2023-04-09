from Models.Expense import Expense
from Models.Context import Session

class ExpenseRepository():
    def __init__(self, db: Session) -> None:
        self.db = db