from pydantic import BaseModel, ValidationError, Field
from Models.Context import DECIMAL 

class ExpenseHeadAmountSaveDto(BaseModel):
    ID: str = Field(max_length=10)
    ExpenseHeadID: str =Field(max_length=10)
    ExpenseLocationID: str =Field(max_length=10)
    Designtaion: str =Field(max_length=50)
    Amount= DECIMAL
    CreatedByID: str =Field(max_length=10)
    UpdatedByID: str =Field(max_length=10, default=None)