from Models.ExpenseHeadAmountSettings import ExpenseHeadAmountSettings,ExpenseHeadAmountSettingsSchema
from Models.Context import Session
from .GenericRepository import GenericRepository

class ExpenseHeadAmountSettingsRepository(GenericRepository):
    def __init__(self, db: Session):
        super().__init__(db, ExpenseHeadAmountSettings, ExpenseHeadAmountSettingsSchema())