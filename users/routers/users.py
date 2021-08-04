from fastapi import  APIRouter
from .. import schemas,database,models,oauth2
from typing import List
from fastapi import FastAPI,Depends,status,Response,HTTPException
from sqlalchemy.orm import Session
from ..hashing import Hash

router=APIRouter(
      tags=['User']
      )


@router.post('/user',status_code=status.HTTP_201_CREATED)
def create(request:schemas.User,db : Session=Depends(database.get_db)):
      new_user=models.Usert(username=request.username,password=Hash.bcrypt(request.password),email_id=request.email_id,address=request.address, phoneno=request. phoneno)
      db.add(new_user)
      db.commit()
      db.refresh(new_user)
      return new_user
#################### Displaying all users       ############################
@router.get('/user',response_model=List[schemas.Show])
def all(db: Session=Depends(database.get_db),get_current_user:schemas.User=Depends(oauth2.get_current_user)):
      users=db.query(models.Usert).all()
      return users


#############################         checking whether user is exisiting or not ###########################
@router.get('/user/{id}', status_code=200,response_model=schemas.Show)
def show(id,response: Response,db: Session=Depends(database.get_db),get_current_user:schemas.User=Depends(oauth2.get_current_user)):
      user=db.query(models.Usert).filter(models.Admin.email_id==id).first()
      if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{user} not existing")
            #response.status_code=status.HTTP_404_NOT_FOUND
            #return{'detail':f"{id} not existing"}
      #raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{user.username} found")
      return user
#####################################        deleting a user ##################################

@router.delete('/admin/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db:Session=Depends(database.get_db),get_current_user:schemas.User=Depends(oauth2.get_current_user)):
      user=db.query(models.Usert).filter(models.Usert.email_id==id)
      if not user.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with{id} not found")
      user.delete(synchronize_session=False)
      db.commit()
      return 'Done'
      
@router.put('/admin/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id, request:schemas.User,db:Session=Depends(database.get_db),get_current_user:schemas.User=Depends(oauth2.get_current_user)):
      u=db.query(models.Usert).filter(models.Usert.email_id==id)
      if not u:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with{id} not found")
      u.update({'password':'Renuka@123'})
      db.commit()
      return 'Updated Sucessfully'
