from Models.ExpenseHeadAmountSettings import ExpenseHeadAmountSettings
from DTO.ExpenseHeadAmountSettingsDto import ExpenseHeadAmountSaveDto, ValidationError, ExpenseHeadAmountUpdateDto
from Models.Context import request, Blueprint, Session
from Services.ExpenseHeadAmountSettingsService import ExpenseHeadAmountSettingsServie

expAmount = Blueprint('expAmount', __name__)

@expAmount.route('/expense/Amount/list', methods = ['GET'])
def getExpense():
    return ExpenseHeadAmountSettingsServie(Session()).getAll() 

@expAmount.route('/expense/Amount/save', methods = ['POST'])
def saveExpense():
    try:
        validatioDto = ExpenseHeadAmountSaveDto(**request.json)
    except ValidationError as e:
        return e.json()
    
    data = ExpenseHeadAmountSettings().getAnObject(dict(validatioDto)) 
    ExpenseHeadAmountSettingsServie(Session()).save(data)   
    
    return "Successfully Saved"

@expAmount.route('/expense/Amount/update', methods =['PUT'])
def updateExpense():
    try:
       
        validatioDto = ExpenseHeadAmountUpdateDto(**request.json)
    except ValidationError as e:
        return e.json()
    
    data = ExpenseHeadAmountSettings().getAnObject(dict(validatioDto))
    ExpenseHeadAmountSettingsServie(Session()).update(data)
    
    return "Successfully Updated"


@expAmount.route('/expense/Amount/delete/<ID>', methods = ['DELETE'])
def deleteExpense(ID):
    ExpenseHeadAmountSettingsServie(Session()).delete(ID)
    return "Successfully Deleted"

@expAmount.route('/expense/Amount/getID/<ID>', methods = ['GET'])
def getByID(ID: str):
    return ExpenseHeadAmountSettingsServie(Session()).getByID(ID)