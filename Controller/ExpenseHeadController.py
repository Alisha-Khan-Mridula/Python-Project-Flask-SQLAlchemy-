from Models.Context import Blueprint, request, Session
from Models.ExpenseHead import ExpenseHead
from DTO.ExpenseHeadDto import ExpenseHeadSaveDto, ValidationError 
from Services.ExpenseHeadService import ExpenseHeadServie

expHead = Blueprint('expHead', __name__)


@expHead.route('/expense/head/list' ,methods = ['GET'])
def getExpenseHeads():
    return ExpenseHeadServie(Session()).getAll()


@expHead.route('/expense/save', methods = ['POST'])
def saveExpense():
    try:
        validatioDto = ExpenseHeadSaveDto(**request.json())
    except ValidationError as e:
        return e.json()
