#============= Importing from Context.py =====================#
from Models.Context import Column, datetime, Integer, Boolean, String, ForeignKey,BaseModel,DateTime,Base, Schema, fields

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
     
     
     
class ExpenseDetailsSchema(Schema):
     ID = fields.Integer()
     ExpenseLocationID = fields.Str()
     ExpenseDate = fields.DateTime()
     LocationFrom = fields.Str()
     LocationTo = fields.Str()
     ExpenseHeadID = fields.Str()
     ExpenseID = fields.Str()
     #ModeOfTransport = fields.Str()
     CreatedByID = fields.Str()
          
    