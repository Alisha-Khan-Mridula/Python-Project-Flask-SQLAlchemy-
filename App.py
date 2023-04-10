# from Migrations.database import createDB
from Models.Context import Session
# import Migrations
from Models.ExpenseHead import ExpenseHead
from Models.Expense import Expense
from Models.ExpenseLocation import ExpenseLocation
from Models.ExpenseDetails import ExpenseDetails
from Models.ExpenseHeadAmountSettings import ExpenseHeadAmountSettings

from Services.ExpenseHeadService import ExpenseHeadServie
from Services.ExpenseService import ExpenseService
from Services.ExpenseLocationService import ExpenseLocationServie
from Services.ExpenseDetailsService import ExpenseDetailsServie
from Services.ExpenseHeadAmountSettingsService import ExpenseHeadAmountSettingsServie

session = Session()
HeadService = ExpenseHeadServie(session)
ExpService = ExpenseService(session)
LocaService = ExpenseLocationServie(session)
DetailsService = ExpenseDetailsServie(session)
AmountService = ExpenseHeadAmountSettingsServie(session)

#createDB()

#=================== Get Data ==================

# data = HeadService.getAll()
# for i in data:
#     print(i.HeadName)
    
#data = ExpService.delete(12)
# data = HeadService.getByID('TA')
# data.HeadName = 'TP'
# new = HeadService.update(data)


#=============== Update Data =============
# new = ExpenseHead(ID ='TA' , HeadName = 'TD')
# data=HeadService.update(new)
# print(data.HeadName)


#================ Delete ==================
# data = HeadService.delete('TA')






#============= Saving ExpenseHead =============
# data = ExpenseHead(ID ="TS3", HeadName = "Test Another", CreatedByID = "LPL02693")
# service.save(data)



# data = ExpenseLocation(ID = 'H.Q.', ShortName = 'H.Q.')
# LocaService.update(data)


# data = DetailsService.getAll()
# for i in data:
#     print(i.ID, i.ExpenseHeadID)


# data = AmountService.getAll()
# for i in data:
#     print(i.ID)







