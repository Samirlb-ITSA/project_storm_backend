from fastapi import APIRouter, HTTPException, Depends
from controllers.career_controller import *
from controllers.auth_controller import AuthController
from models.career_model import CareerIn
from models.user_model import User

router = APIRouter()

new_career = CareerController()
auth_controller = AuthController()

@router.post("/create_career")
async def create_career(career: CareerIn, current_user: User = Depends(auth_controller.get_current_active_user)):
    response = new_career.create_career(career)
    return response

@router.get("/get_career/{career_id}",response_model=CareerIn)
async def get_career(career_id: int, current_user: User = Depends(auth_controller.get_current_active_user)):
    response = new_career.get_career(career_id)
    return response

@router.get("/get_careers/")
async def get_careers(current_user: User = Depends(auth_controller.get_current_active_user)):
    response = new_career.get_careers()
    return response

@router.put("/update_career")
async def update_career(career: CareerIn, current_user: User = Depends(auth_controller.get_current_active_user)):
    response = new_career.update_career(career)
    return response

@router.delete("/delete_career/{career_id}")
async def delete_career(career_id: int, current_user: User = Depends(auth_controller.get_current_active_user)):
    response = new_career.delete_career(career_id)
    return response