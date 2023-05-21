from pydantic import BaseModel, ValidationError, Field



class ExpenseLocationSaveDto(BaseModel):
    ID: str =Field(max_length=10)
    LocationName: str= Field(min_length=4, max_length=50)
    ShortName: str 
    CreatedByID: str = Field(min_length=4, max_length=50)
    UpdatedByID: str