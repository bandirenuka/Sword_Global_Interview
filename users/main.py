from typing import List
from fastapi import FastAPI,Depends,status,Response,HTTPException
from . import schemas,models
#from . database import engine, SessionLocal,get_db
from sqlalchemy.orm import Session
from .hashing import Hash
from .routers import users,login
from .database import engine, SessionLocal






      
################# initializing FastAPI  to app#############################
app=FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(login.router)
app.include_router(users.router)






