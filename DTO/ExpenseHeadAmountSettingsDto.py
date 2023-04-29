from pydantic import BaseModel, ValidationError, Field
from Models.Context import DECIMAL 

class ExpenseHeadAmountSaveDto(BaseModel):
    ID: str = Field(max_length=10)
    ExpenseHeadID: str =Field(max_length=10)
    ExpenseLocationID: str =Field(max_length=10)
    Designation: str =Field(max_length=50)
    Amount= int
    CreatedByID: str =Field(max_length=10)
    #UpdatedByID: str =Field(max_length=10, default=None)
    
class ExpenseHeadAmountUpdateDto(BaseModel):
    ID: str = Field(max_length=10)
    Designation: str =Field(max_length=50)
    #Amount: int
    