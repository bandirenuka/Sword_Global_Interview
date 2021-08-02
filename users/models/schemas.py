from pydantic import BaseModel
from typing import List,Optional

class User(BaseModel):
      name:str
      email:str
      password:str
      address:str
      telephone_number:str
