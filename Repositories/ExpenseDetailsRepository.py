from Models.ExpenseDetails import ExpenseDetails
from Models.Context import Session

class ExpenseDetailsRepository():
    def __init__(self, db: Session) -> None:
        self.db = db
        
