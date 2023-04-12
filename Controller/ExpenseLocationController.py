from Models.ExpenseLocation import ExpenseLocation
from Services.ExpenseLocationService import ExpenseLocationServie
from DTO.ExpenseLocationDto import ExpenseLocationSaveDto, ValidationError
from Models.Context import Blueprint,Session, request

expLocation = Blueprint('expLocation', __name__)

@expLocation.route('/location/list', methods = ['GET'])
def getLocation():
    return ExpenseLocationServie(Session()).getAll() 

@expLocation.route('/location/save', methods = ['POST'])
def saveLocation():
    try:
        validationDto = ExpenseLocationSaveDto(**request.json)
        
    except ValidationError as e:
        return e.json()
    
    data = ExpenseLocation().getAnObject(dict(validationDto))    
    ExpenseLocationServie(Session()).save(data)
    return "Successfully Saved" 

@expLocation.route('/location/update', methods =['PUT'])
def updateLocation():
    try:
        validationDto = ExpenseLocationSaveDto(**request.json)
        
    except ValidationError as e:
        return e.json()
    
    data = ExpenseLocation().getAnObject(dict(validationDto))
    ExpenseLocationServie(Session()).update(data)
    return "Successfully Updated"     


@expLocation.route('/location/delete/<ID>', methods =['DELETE'])
def deleteLocation(ID : str):
    ExpenseLocationServie(Session()).delete(ID)
    return "Delete Successfully"