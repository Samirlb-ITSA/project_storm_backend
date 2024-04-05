from fastapi import APIRouter, HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from models.user_model import User
from models.role_model import RoleIn
from routes.user_routes import UserController
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError
from dotenv import load_dotenv
import os

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from typing import List
from passlib.context import CryptContext


load_dotenv()


router = APIRouter()
controller = UserController()
users = controller.getUsersFromDb()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


class AuthController:
    async def authenticate(self, form_data: OAuth2PasswordRequestForm = Depends()):
        user = self.authenticate_user(users, form_data.username, form_data.password)
        access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
        role_in_list = jsonable_encoder([RoleIn(roleid=str(role.roleid), name=role.name) for role in user.roles])
        access_token = self.create_access_token(
            data={"id": str(user.userid), "first_name": user.firstname, "last_name": user.lastname, "roles": role_in_list}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}

    def get_user(self, db, userid):
        return next((user for user in db if str(user.userid) == userid), [])

    def get_user_form_email(self, db, email):
        return next((user for user in db if user.email == email), [])

    def authenticate_user(self, db, email, password):
        user = self.get_user_form_email(db, email)
        if not user:
            raise HTTPException(status_code = 401, detail= "Could not validate credentials", headers={"WWW-Autenticate": "Bearer"})
        if not self.verify_password(password, user.password):
            raise HTTPException(status_code = 401, detail ="Could not validate credentials", headers={"WWW-Autenticate": "Bearer"})
        return user
        
    def verify_password(self, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    def create_access_token(self, data: dict, expires_delta: timedelta ):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=15)
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        encoded_token_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
        return encoded_token_jwt

    async def get_current_user(self, token: str = Depends(oauth2_scheme)):
        credentials_exception = HTTPException(
            status_code = 401,
            detail = "Could not validate credentials",
            headers = {"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            userid: str = payload.get("id")
            if userid is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        user = self.get_user(users, userid)
        if user is None:
            raise credentials_exception
        return user

    async def get_current_active_user(self, token: str = Depends(oauth2_scheme)):
        current_user = await self.get_current_user(token)
        if current_user.status == False :
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user