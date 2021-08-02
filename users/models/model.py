from sqlalchemy import Column,Integer,String
from .database import Base




class Usert(Base):
      __tablename__='users'
      username=Column(String(50))
      email_id=Column(String(50),primary_key=True,index=True)
      password=Column(String(550))
      address=Column(String(50))
      phoneno=Column(String(50))
