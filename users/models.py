from typing import Text
from sqlalchemy import Column,Integer,String
from sqlalchemy.sql.type_api import STRINGTYPE
from .database import Base




class Usert(Base):
      __tablename__='users'
      username=Column(String(50))
      password=Column(String(250))
      email_id=Column(String(50),primary_key=True,index=True)
      address=Column(String(50))
      phoneno=Column(String(50))


