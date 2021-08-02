from fastapi import FastAPI,Depends,status,Response,HTTPException
from pydantic import BaseModel
from models import model,schemas,database
from models.database import engine
from sqlalchemy.orm import Session
from models.database import get_db



app=FastAPI()

model.Base.metadata.create_all(bind=engine)




@app.post('/user',status_code=status.HTTP_201_CREATED)
def create_user(request:schemas.User,db:Session=Depends(get_db)):
      new_user=model.Usert(username=request.name,email_id=request.email,password=request.password,address=request.address,phoneno=request.telephone_number)
      db.add(new_user)
      db.commit()
      db.refresh(new_user)
      return new_user


@app.get("/users")
def all_users(db:Session=Depends(get_db)):
      users=db.query(model.Usert).all()
      return users


@app.put('/user/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.User,db:Session=Depends(get_db)):
     user=db.query(model.Usert).filter(model.Usert.email_id==id)
     if not user:
           raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with{id} not found")
     user.update({'address':'Heaven'})
     db.commit()
     return "updated"

@app.delete('/user/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id,db:Session=Depends(get_db)):
      db.query(model.Usert).filter(model.Usert.email_id==id).delete(synchronize_session=False)
      db.commit()
      
      return {"status":"Done"}
      

                            
@app.get('/user/{id}',status_code=200)
def index(id,response:Response,db:Session=Depends(get_db)):
      users=db.query(model.Usert).filter(model.Usert.email_id==id).first()
      if not users:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with the emaild id {id} is not exissting")
            

      return users



