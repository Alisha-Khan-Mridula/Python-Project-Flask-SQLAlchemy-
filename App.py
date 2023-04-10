# from Migrations.database import createDB
from Models.Context import Session
# import Migrations
from Repositories.ExpenseHeadRepository import ExpenseHeadRepository
from Models.ExpenseHead import ExpenseHead
from Repositories.GenericRepository import GenericRepository
session = Session()


HeadRepo = ExpenseHeadRepository(session)
# ExpenseRepo = ExpenseRepository(session)
# LocationRepo = ExpenseLocationReposotory(session)
# AmountRepo = ExpenseHeadAmountSettingsRepository(session)
# DetailsRepo = ExpenseDetailsRepository(session)


#createDB()

# data = HeadRepo.getAll()
# for i in data:
#     print(i.ID)


# item = ExpenseHead(ID = "TS3", HeadName = "Test Another", CreatedByID = "LPL02693")

# GenericRepository.save(item)





