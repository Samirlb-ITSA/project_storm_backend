from fastapi import APIRouter, HTTPException, Depends
from controllers.aplicante_controller import *
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from models.user_model import User
from routes.user_routes import UserController
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError
from dotenv import load_dotenv
import os

load_dotenv()


router = APIRouter()

controller = UserController()
users = controller.getUsersFromDb()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

@router.post("/login")
async def authenticate(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(users, form_data.username, form_data.password)
    access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = create_access_token(
        data={"sub": user.correo}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

def get_user(db, username):
    return next((user for user in db if user.correo == username), [])

def authenticate_user(db, username, password):
    user = get_user(db, username)
    if not user:
        raise HTTPException(status_code = 401, detail= "Could not validate credentials", headers={"WWW-Autenticate": "Bearer"})
    if not verify_password(password, user.contraseña):
        raise HTTPException(status_code = 401, detail ="Could not validate credentials", headers={"WWW-Autenticate": "Bearer"})
    return user
    
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=15)
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_token_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
    return encoded_token_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code = 401,
        detail = "Could not validate credentials",
        headers = {"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(users, username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.estado == 0 :
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
