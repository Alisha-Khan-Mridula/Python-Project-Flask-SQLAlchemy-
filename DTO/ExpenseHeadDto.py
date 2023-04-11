from pydantic import BaseModel, ValidationError, Field

class ExpenseHeadSaveDto(BaseModel):
    ID: str = Field(min_length=2)
    HeadName: str =Field(min_length=4, max_length=50)
    CreatedByID: str
    
  