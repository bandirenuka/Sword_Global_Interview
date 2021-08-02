from fastapi import FastAPI,Depends
from pydantic import BaseModel
from models import model,schemas,database
from models.database import engine
from sqlalchemy.orm import Session
from models.database import get_db



app=FastAPI()

model.Base.metadata.create_all(bind=engine)




@app.post('/user')
def create_user(request:schemas.User,db:Session=Depends(get_db)):
      new_user=model.Usert(username=request.name,email_id=request.email,address=request.address,phoneno=request.telephone_number)
      db.add(new_user)
      db.commit()
      return new_user


@app.get("/users")
def all_users(db:Session=Depends(get_db)):
      users=db.query(model.Usert).all()
      return users
      

                            
@app.get('/user/{id}')
def index(id,db:Session=Depends(get_db)):
      users=db.query(model.Usert).filter(model.Usert.username==id).first()
      return users



