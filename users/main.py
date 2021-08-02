from fastapi import FastAPI
from pydantic import BaseModel


app=FastAPI()

@app.get("/user/{id}")
def index():
      return "Oh God"


@app.get("/users")
def all_users():
      return "all users"

class User(BaseModel):
      name:str
      email:str
      address:str
      telephone_number:str


@app.post('/user')
def create_user(request:User):
      return {}

