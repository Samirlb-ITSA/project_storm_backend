from fastapi import APIRouter, HTTPException, Form, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from controllers.user_controller import *
from models.user_model import User
from models.login_model import Login

router = APIRouter()

nuevo_usuario = UserController()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


@router.post("/create_user")
async def create_user(user: User):
    rpta = nuevo_usuario.create_user(user)
    return rpta


@router.get("/get_user/{user_id}",response_model=User)
async def get_user(user_id: int, token: str = Depends(oauth2_scheme)):
    rpta = nuevo_usuario.get_user(user_id)
    return rpta

@router.get("/get_users/")
async def get_users():
    rpta = nuevo_usuario.get_users()
    return rpta

@router.put("/update_user")
async def update_user(user: User):
    rpta = nuevo_usuario.update_user(user)
    return rpta

@router.delete("/delete_user/{user_id}")
async def delete_user(user_id: int):
    rpta = nuevo_usuario.delete_user(user_id)
    return rpta

@router.post("/login")
async def login(login: Login):
    user_data = nuevo_usuario.authenticate_user(login)
    return user_data