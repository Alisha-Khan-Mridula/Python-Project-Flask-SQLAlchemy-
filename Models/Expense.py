#============= Importing from Context.py =====================#
from Models.Context import Column, datetime, Integer, Boolean, String, ForeignKey,BaseModel,DateTime,Base


#============ Expense Model Creation ================#
class Expense(Base,BaseModel):
    
    __tablename__ = 'Expense' 
    ID = Column(Integer, primary_key=True, autoincrement= True)
    EmployeeID = Column(String(20), unique= True, nullable=False)
    ExpenseMonth = Column(DateTime(), default = datetime.now)
    CheckedByID = Column (String(10))
    CheckedOn = Column(DateTime())
    VerifiedByID = Column(String(10), nullable=True)
    VerifiedOn = Column(DateTime())
    ForwardedByID = Column(String(10), nullable=True)
    ForwardedOn = Column(DateTime())
    RecommendedByID = Column(String(10), nullable=True)
    RecommendedOn = Column(DateTime())
    ApprovedByID = Column(String(10), nullable=True)
    ApprovedOn = Column(DateTime())
    FCAApprovedByID = Column(String(10), nullable=True)
    FCAApprovedOn = Column(DateTime())
    FAApprovedByID = Column(String(10), nullable=True)
    FAApprovedOn = Column(DateTime())
    ManagementApprovedByID = Column(String(10),nullable=True)
    ManagementApprovedOn = Column(DateTime())