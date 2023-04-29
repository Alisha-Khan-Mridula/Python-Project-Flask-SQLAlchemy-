from pydantic import BaseModel, ValidationError, Field
from datetime import datetime


class ExpenseDetailsSaveDto(BaseModel):
    #ID: int 
    ExpenseLocationID: str = Field(min_length=4, max_length=50)
    Expensedate: datetime = Field(default_factory=datetime.now)
    LocationFrom: str = Field(min_length=4, max_length=50)
    LocationTo: str = Field(min_length=4, max_length=50)
    ExpenseHeadID: str = Field( max_length=50)
    ExpenseID: int 
    ModeOfTransport: str =Field(min_length=4, max_length=20)
    CreatedByID: str = Field(min_length=4, max_length=50)
    #UpdatedByID: str = Field(min_length=4, max_length=10)
    

class ExpenseDetailsUpdateDto(BaseModel):
    ID: int
    LocationFrom: str = Field(min_length=4, max_length=50)
    
    