from Models.Context import Blueprint, request, Session
from Models.ExpenseHead import ExpenseHead
from DTO.ExpenseHeadDto import ExpenseHeadSaveDto, ValidationError 
from Services.ExpenseHeadService import ExpenseHeadServie

expHead = Blueprint('expHead', __name__)


@expHead.route('/expense/head/list' ,methods = ['GET'])
def getExpenseHeads():
    return ExpenseHeadServie(Session()).getAll()


@expHead.route('/expense/head/save', methods = ['POST'])
def saveExpense():
    try:
        validatioDto = ExpenseHeadSaveDto(**request.json)
    except ValidationError as e:
        return e.json()
    
    data = ExpenseHead().getAnObject(dict(validatioDto))
    ExpenseHeadServie(Session()).save(data)
    return "Successfully saved"

@expHead.route('/expense/head/update', methods =['PUT'])
def updateExpenseHead():
    try:
        validatioDto = ExpenseHeadSaveDto(**request.json)
    except ValidationError as e:
        return e.json()
    
    
    data = ExpenseHead().getAnObject(dict(validatioDto))
    ExpenseHeadServie(Session()).update(data)
    return "Successfully Updated"    

@expHead.route('/expense/head/delete/<ExpenseHeadID>', methods = ['DELETE'])
def deleteExpenseHead(ExpenseHeadID : str):
    ExpenseHeadServie(Session()).delete(ExpenseHeadID)
    return "Successfully Deleted"

 
        