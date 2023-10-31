from fastapi import APIRouter, HTTPException, Depends
from controllers.aplicante_controller import *
from models.aplicante_model import Aplicante
from fastapi.security import OAuth2PasswordRequestForm
from models.user_model import User
from routes.user_routes import UserController
from passlib.context import CryptContext
from pydantic import BaseModel


router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/token")
async def authenticate(form_data: OAuth2PasswordRequestForm = Depends()):
    controller = UserController()
    users = controller.getUsersFromDb()
    print(form_data.username, form_data.password)
    user = authenticate_user(users, form_data.username, form_data.password)
    return {"access_token": "access_token", "token_type": "bearer"}

def get_user(db, username):
    return next((user for user in db if user.nombre == username), [])

def authenticate_user(db, username, password):
    user = get_user(db, username)
    if not user:
        raise HTTPException(status_code = 401, detail= "Could not validate credentials", headers={"WWW-Autenticate": "Bearer"})
    if not verify_password(password, user.contraseña):
        raise HTTPException(status_code = 401, detail ="Could not validate credentials", headers={"WWW-Autenticate": "Bearer"})
    return user
    
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)