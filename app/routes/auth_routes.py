from fastapi import APIRouter, HTTPException, Depends
from controllers.applicant_controller import *
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from models.user_model import User
from routes.user_routes import UserController
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError
from dotenv import load_dotenv
from controllers.auth_controller import AuthController
import os

load_dotenv()


router = APIRouter()

auth_controller = AuthController()

@router.post("/login")
async def authenticate_route(form_data: OAuth2PasswordRequestForm = Depends()):
    response = await auth_controller.authenticate(form_data) 
    return response