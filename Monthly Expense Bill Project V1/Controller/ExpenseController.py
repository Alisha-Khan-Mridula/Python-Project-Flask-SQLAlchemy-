from Models.Expense import Expense, ExpenseSchema
from DTO.ExpenseDto import ExpenseSaveDto, ValidationError, ExpenseUpdateDto
from Models.Context import request, Blueprint, Session
from Services.ExpenseService import ExpenseService


exp = Blueprint('exp', __name__)

@exp.route('/expense/list', methods = ['GET'])
def getExpense():
    return ExpenseService(Session()).getAll() 

@exp.route('/expense/save', methods = ['POST'])
def saveExpense():
    try:
        validatioDto = ExpenseSaveDto(**request.json)
    except ValidationError as e:
        return e.json()
    
    data = Expense().getAnObject(dict(validatioDto)) 
    ExpenseService(Session()).save(data)   
    
    return "Successfully Saved"

@exp.route('/expense/update', methods =['PUT'])
def updateExpense():
    try:
       
        validatioDto = ExpenseUpdateDto(**request.json)
    except ValidationError as e:
        return e.json()
    
    data = Expense().getAnObject(dict(validatioDto))
    ExpenseService(Session()).update(data)
    
    return "Successfully Updated"


@exp.route('/expense/delete/<ID>', methods = ['DELETE'])
def deleteExpense(ID: int):
    ExpenseService(Session()).delete(ID)
    return "Successfully Deleted" 

@exp.route('/expense/getID/<ID>', methods = ['GET'])
def getByID(ID: int):
    return ExpenseService(Session()).getByID(ID)