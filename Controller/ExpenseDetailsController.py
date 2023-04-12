from Models.ExpenseDetails import ExpenseDetails
from DTO.ExpenseDetailsDto import ExpenseDetailsSaveDto, ValidationError
from Models.Context import request, Blueprint, Session
from Services.ExpenseDetailsService import ExpenseDetailsServie

expDetails = Blueprint('expDetails', __name__)

@expDetails.route('/expense/Details/list', methods = ['GET'])
def getExpense():
    return ExpenseDetailsServie(Session()).getAll() 

@expDetails.route('/expense/Details/save', methods = ['POST'])
def saveExpense():
    try:
        validatioDto = ExpenseDetailsSaveDto(**request.json)
    except ValidationError as e:
        return e.json()
    
    data = ExpenseDetailsSaveDto().getAnObject(dict(validatioDto)) 
    ExpenseDetailsServie(Session()).save(data)   
    
    return "Successfully Saved"

@expDetails.route('/expense/Details/update', methods =['PUT'])
def updateExpense():
    try:
       
        validatioDto = ExpenseDetailsSaveDto(**request.json)
    except ValidationError as e:
        return e.json()
    
    data = ExpenseDetailsSaveDto().getAnObject(dict(validatioDto))
    ExpenseDetailsServie(Session()).update(data)
    
    return "Successfully Updated"


@expDetails.route('/expense/Details/delete/<ID>', methods = ['DELETE'])
def deleteExpense(ID):
    ExpenseDetailsServie(Session()).delete(ID)
    return "Successfully Deleted"
