#============= Importing from Context.py =====================#
from Models.Context import Column, datetime, Integer, Boolean, String, ForeignKey,BaseModel,DateTime,DECIMAL,Base,Schema, fields


#============ ExpenseLocation Model Creation ================#

class ExpenseLocation(Base,BaseModel):
    __tablename__ = 'ExpenseLocation'
    ID = Column(String(10), primary_key=True)
    LocationName = Column(String(50), nullable=True)
    ShortName = Column(String(50), nullable=True)
    
    
class ExpenseLocationSchema(Schema):
    ID =fields.Str()
    #LocationName = fields.Str()
    ShortName = fields.Str()
    CreatedByID = fields.Str()
    #UpdatedByID = fields.Str()
    IsActive = fields.Boolean()   