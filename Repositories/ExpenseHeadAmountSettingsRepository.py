from Models.ExpenseHeadAmountSettings import ExpenseHeadAmountSettings
from Models.Context import Session

class ExpenseHeadAmountSettingsRepository():
    def __init__(self, db: Session) -> None:
        self.db = db