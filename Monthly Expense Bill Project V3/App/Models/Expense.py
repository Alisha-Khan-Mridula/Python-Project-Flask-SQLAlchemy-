from .BaseModel import BaseModel
from App.database import Base
from sqlalchemy import String, Boolean, Integer, DateTime, Column, ForeignKey
from datetime import datetime


class Expense(Base,BaseModel):
    
    __tablename__ = 'Expense' 
    ID = Column(Integer, primary_key=True, autoincrement= True)
    EmployeeID = Column(String(20), unique= True, nullable=False)
    ExpenseMonth = Column(DateTime())
    CheckedByID = Column (String(10))
    CheckedOn = Column(DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    
    
    VerifiedByID = Column(String(10), nullable=True)
    VerifiedOn = Column(DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    
    
    ForwardedByID = Column(String(10), nullable=True)
    ForwardedOn = Column(DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    
    
    RecommendedByID = Column(String(10), nullable=True)
    RecommendedOn = Column(DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    
    
    ApprovedByID = Column(String(10), nullable=True)
    ApprovedOn = Column(DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    
    
    FCAApprovedByID = Column(String(10), nullable=True)
    FCAApprovedOn = Column(DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    
    
    FAApprovedByID = Column(String(10), nullable=True)
    FAApprovedOn = Column(DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    
    
    ManagementApprovedByID = Column(String(10),nullable=True)
    ManagementApprovedOn = Column(DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    