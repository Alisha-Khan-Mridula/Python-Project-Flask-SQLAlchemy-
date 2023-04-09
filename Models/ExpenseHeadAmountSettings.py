#============= Importing from Context.py =====================#
from Models.Context import Column, datetime, Integer, Boolean, String, ForeignKey,BaseModel,DateTime,DECIMAL, Base


#============ ExpenseHeadAmountSettings Model Creation ================#
class ExpenseHeadAmountSettings(Base,BaseModel):
    __tablename__ = 'ExpenseHeadAmountSettings'  
    ID = Column(String(10), primary_key=True)
    ExpenseHeadID = Column(String(10), ForeignKey('ExpenseHead.ID'))
    ExpenseLocationID = Column(String(10), ForeignKey('ExpenseLocation.ID'))
    Designation = Column(String(50))
    Amount = Column(DECIMAL)