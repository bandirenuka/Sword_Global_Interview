from pydantic import BaseModel
from typing import List,Optional

class User(BaseModel):
      name:str
      email:str
      password:str
      address:str
      telephone_number:str
      class Config():
            orm_mode=True
            
class Show(BaseModel):
      name:str
      email:str
      
      
      class Config():
            orm_mode=True
      
      
      
