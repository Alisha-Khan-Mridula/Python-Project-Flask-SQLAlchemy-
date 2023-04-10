from Models.ExpenseHeadAmountSettings import ExpenseHeadAmountSettings
from Models.Context import Session
from .GenericRepository import GenericRepository

class ExpenseHeadAmountSettingsRepository(GenericRepository):
    def __init__(self, db: Session) -> None:
        super().__init__(db, ExpenseHeadAmountSettings)