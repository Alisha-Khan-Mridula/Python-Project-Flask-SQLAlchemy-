from sqlalchemy import Column, Integer, Boolean, String, ForeignKey,DECIMAL 
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy import create_engine
import urllib
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import List
from marshmallow import Schema, fields
from flask import Blueprint, request





Base = declarative_base()
engine = create_engine('sqlite:///App/Database//MonthlyExpenseBill.db')    
Session = sessionmaker(bind=engine)