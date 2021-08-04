from pydantic import BaseModel
from typing import List,Optional
class User(BaseModel):
      username:str
      password:str
      email_id:str
      address:str
      phoneno:str

class Login(BaseModel):
      email_id:str
      password:str

class Show(BaseModel):
      username:str
      email_id:str
      class Config():
            orm_mode=True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email_id: Optional[str] = None
  
