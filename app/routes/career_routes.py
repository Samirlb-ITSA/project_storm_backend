from fastapi import APIRouter, HTTPException
from controllers.career_controller import *
from models.career_model import CareerIn

router = APIRouter()

new_career = CareerController()


@router.post("/create_career")
async def create_career(career: CareerIn):
    response = new_career.create_career(career)
    return response


@router.get("/get_career/{career_id}",response_model=CareerIn)
async def get_career(career_id: int):
    response = new_career.get_career(career_id)
    return response

@router.get("/get_careers/")
async def get_careers():
    response = new_career.get_careers()
    return response

@router.put("/update_career")
async def update_career(career: CareerIn):
    response = new_career.update_career(career)
    return response

@router.delete("/delete_career/{career_id}")
async def delete_career(career_id: int):
    response = new_career.delete_career(career_id)
    return response