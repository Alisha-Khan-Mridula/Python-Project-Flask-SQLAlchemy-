#===================== Importing All The commom classes ==========================#

from sqlalchemy import Column, Integer, Boolean, String, ForeignKey,DECIMAL 
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy import create_engine
import urllib
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import List
from marshmallow import Schema, fields
from flask import Blueprint, request


#==================== Base Model Class Creation ============================#

class BaseModel():  # BaseModel class is the class of the common Fields of all the models
    IsActive = Column(Boolean, default=True)
    CreatedByID = Column(String(10), nullable=False)
    CreatedOn = Column(DateTime(), default=datetime.now)
    UpdatedByID = Column(String(10),nullable=True)
    UpdatedOn = Column(DateTime(),  onupdate=datetime.now)

Base = declarative_base()


#==================== Connecting With the Server ===========================#
server = *****
username = ***
password = *****
database = *****

connectionString = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=Sql Server"
engine = create_engine(connectionString, pool_recycle = 3600, echo=True, use_setinputsizes=False)

#engine = create_engine('sqlite:///Database//sales.db')  
Session = sessionmaker(bind=engine)
