from typing import List
from fastapi import FastAPI,Depends,status,Response,HTTPException
from . import schemas,models
#from . database import engine, SessionLocal,get_db
from sqlalchemy.orm import Session
from .hashing import Hash
from .routers import users,login
from .database import engine, SessionLocal


origins = [

    "http://localhost:3000"

]



app.add_middleware(

    CORSMiddleware,

    allow_origins=['*'],

    allow_credentials=True,

    allow_methods=['*'],

    allow_headers=['*'],

)



      
################# initializing FastAPI  to app#############################
app=FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(login.router)
app.include_router(users.router)






