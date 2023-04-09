from Models.ExpenseLocation import ExpenseLocation
from Models.Context import Session

class ExpenseLocationRepository():
    def __init__(self, db: Session) -> None:
        self.db = db