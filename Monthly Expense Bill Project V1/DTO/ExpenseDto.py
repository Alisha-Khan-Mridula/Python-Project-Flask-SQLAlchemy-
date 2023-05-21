from pydantic import BaseModel, ValidationError, Field, validator
from datetime import datetime,date


class ExpenseSaveDto(BaseModel):
    #ID: int
    EmployeeID: str = Field(min_length=7, max_length=20)
    ExpenseMonth: str =Field(default=None)
    CheckedByID: str = Field(max_length=10,default=None)
    VerifiedByID: str = Field(max_length=10, default=None)
    ForwardedByID:str = Field(max_length=10, default=None)
    RecommendedByID:str = Field(max_length=10, default=None)
    ApprovedByID: str = Field(max_length=10, default=None)
    FCAApprovedByID:str = Field(max_length=10, default=None)
    FAApprovedByID:str = Field(max_length=10, default=None)
    ManagementApprovedByID:str = Field(max_length=10, default=None)
    UpdatedByID:  str = Field(max_length=10, default=None)    
    CreatedByID: str = Field(max_length=10, default=None) 
    
    
    
    
    # @validator('ExpenseMonth')
    # def parse_date(cls, value):
    #     if isinstance(value, datetime):
    #         return value
    #     try:
    #         return datetime.fromisoformat(value)
    #     except ValueError:
    #         raise ValueError('invalid datetime format')
    
    @validator('ExpenseMonth')
    def parse_date(cls, value):
        if isinstance(value, date):
            value = value.strftime('%Y-%m-%d')
        return value
    
    
    
class ExpenseUpdateDto(BaseModel):
    ID: int
    EmployeeID: str = Field(min_length=7, max_length=20)
    