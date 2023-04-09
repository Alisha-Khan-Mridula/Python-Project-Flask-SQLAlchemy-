#============= Importing from Context.py =====================#
from Models.Context import Column, datetime, Integer, Boolean, String, ForeignKey,BaseModel,DateTime,Base

#============ ExpenseDetails Model Creation ================#
class ExpenseDetails(Base,BaseModel):
     __tablename__ = 'ExpenseDetails'
     ID = Column(Integer, primary_key =True, autoincrement=True)
     ExpenseLocationID = Column(String(10), ForeignKey('ExpenseLocation.ID'))
     ExpenseDate = Column(DateTime())
     LocationFrom = Column(String(50))
     LocationTo = Column(String(50))
     ExpenseHeadID = Column(String(10), ForeignKey('ExpenseHead.ID'))
     ExpenseID = Column(Integer, ForeignKey('Expense.ID'))
     ModeOfTransport = Column(String(20), nullable=True)
    