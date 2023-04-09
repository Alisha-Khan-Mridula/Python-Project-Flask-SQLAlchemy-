from Models.ExpenseHead import ExpenseHead
from Models.Context import Session

class ExpenseHeadRepository():
    def __init__(self, db: Session) -> None:
        self.db = db