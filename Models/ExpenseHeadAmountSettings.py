#============= Importing from Context.py =====================#
from Models.Context import Column, datetime, Integer, Boolean, String, ForeignKey,BaseModel,DateTime,DECIMAL, Base, Schema, fields


#============ ExpenseHeadAmountSettings Model Creation ================#
class ExpenseHeadAmountSettings(Base,BaseModel):
    __tablename__ = 'ExpenseHeadAmountSettings'  
    ID = Column(String(10), primary_key=True)
    ExpenseHeadID = Column(String(10), ForeignKey('ExpenseHead.ID'))
    ExpenseLocationID = Column(String(10), ForeignKey('ExpenseLocation.ID'))
    Designation = Column(String(50))
    Amount = Column(DECIMAL)
    
    
class ExpenseHeadAmountSettingsSchema(Schema):
    ID = fields.Str()
    ExpenseHeadID = fields.Str()
    ExpenseLocationID = fields.Str()
    Designation = fields.Str()
    Amount = fields.Decimal()
    CreatedByID = fields.Str()
         