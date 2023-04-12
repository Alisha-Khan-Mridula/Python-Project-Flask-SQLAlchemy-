#============= Importing from Context.py =====================#
from Models.Context import Column, datetime, Integer, Boolean, String, ForeignKey,BaseModel,DateTime,Base, Schema, fields


#============ ExpenseHead Model Creation ================#
class ExpenseHead(Base,BaseModel):
    __tablename__ = 'ExpenseHead'
    ID = Column(String(10), primary_key= True)
    HeadName = Column(String(20), nullable= True)
    
    
class ExpenseHeadSchema(Schema):
    ID = fields.Str()
    #HeadName = fields.Str()
    CreatedByID = fields.Str()
    #UpdatedByID = fields.Str()
    IsActive = fields.Boolean()
        