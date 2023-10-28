from fastapi import APIRouter, HTTPException
from controllers.carrera_controller import *
from models.carrera_model import Carrera

router = APIRouter()

nuevo_carrera = CarreraController()


@router.post("/create_carrera")
async def create_carrera(carrera: Carrera):
    rpta = nuevo_carrera.create_carrera(carrera)
    return rpta


@router.get("/get_carrera/{carrera_id}",response_model=Carrera)
async def get_carrera(carrera_id: int):
    rpta = nuevo_carrera.get_carrera(carrera_id)
    return rpta

@router.get("/get_carreras/")
async def get_carreras():
    rpta = nuevo_carrera.get_carreras()
    return rpta

@router.put("/update_carrera")
async def update_carrera(carrera: Carrera):
    rpta = nuevo_carrera.update_carrera(carrera)
    return rpta

@router.delete("/delete_carrera/{carrera_id}")
async def delete_carrera(carrera_id: int):
    rpta = nuevo_carrera.delete_carrera(carrera_id)
    return rpta
