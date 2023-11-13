from fastapi import APIRouter, HTTPException, Depends
from controllers.applicant_controller import *
from controllers.auth_controller import AuthController
from models.applicant_model import ApplicantIn
from models.user_model import User

router = APIRouter()

new_applicant = ApplicantController()
auth_controller = AuthController()

@router.post("/create_applicant")
async def create_applicant(applicant: ApplicantIn, current_user: User = Depends(auth_controller.get_current_active_user)):
    response = new_applicant.create_applicant(applicant)
    return response

@router.get("/get_applicant/{applicant_id}",response_model=ApplicantIn)
async def get_applicant(applicant_id: int, current_user: User = Depends(auth_controller.get_current_active_user)):
    response = new_applicant.get_applicant(applicant_id)
    return response

@router.get("/get_applicants/")
async def get_applicants(current_user: User = Depends(auth_controller.get_current_active_user)):
    response = new_applicant.get_applicants()
    return response

@router.put("/update_applicant")
async def update_applicant(applicant: ApplicantIn, current_user: User = Depends(auth_controller.get_current_active_user)):
    response = new_applicant.update_applicant(applicant)
    return response

@router.delete("/delete_applicant/{applicant_id}")
async def delete_applicant(applicant_id: int, current_user: User = Depends(auth_controller.get_current_active_user)):
    response = new_applicant.delete_applicant(applicant_id)
    return response