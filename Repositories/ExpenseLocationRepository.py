from Models.ExpenseLocation import ExpenseLocation
from Models.Context import Session
from .GenericRepository import GenericRepository

class ExpenseLocationRepository(GenericRepository):
    def __init__(self, db: Session) -> None:
        super().__init__(db, ExpenseLocation )