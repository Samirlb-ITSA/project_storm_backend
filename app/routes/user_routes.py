from fastapi import APIRouter, Depends, UploadFile
from fastapi.security import OAuth2PasswordBearer
from controllers.user_controller import *
from models.user_model import UserIn
from models.login_model import Login
from controllers.auth_controller import AuthController
from models.user_model import User

router = APIRouter()

new_user = UserController()
auth_controller = AuthController()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

@router.post("/create_user")
async def create_user(user: UserIn, current_user: User = Depends(auth_controller.get_current_active_user)):
    response = new_user.create_user(user)
    return response

@router.get("/get_user/{user_id}",response_model=UserIn)
async def get_user(user_id: str, current_user: User = Depends(auth_controller.get_current_active_user)):
    response = new_user.get_user(user_id)
    return response

@router.get("/get_users/")
async def get_users(current_user: User = Depends(auth_controller.get_current_active_user)):
    response = new_user.get_users()
    return response

@router.put("/update_user")
async def update_user(user: UserIn, current_user: User = Depends(auth_controller.get_current_active_user)):
    response = new_user.update_user(user)
    return response

@router.delete("/delete_user/{user_id}")
async def delete_user(user_id: str, current_user: User = Depends(auth_controller.get_current_active_user)):
    response = new_user.delete_user(user_id)
    return response


@router.post("/users/import")
async def import_users(file: UploadFile = File(...), current_user: User = Depends(auth_controller.get_current_active_user)):
    response = new_user.import_users(file)
    return response