from fastapi import APIRouter, HTTPException
from controllers.aplicante_controller import *
from models.aplicante_model import Aplicante

router = APIRouter()

nuevo_aplicante = AplicanteController()


@router.post("/create_aplicante")
async def create_aplicante(aplicante: Aplicante):
    rpta = nuevo_aplicante.create_aplicante(aplicante)
    return rpta


@router.get("/get_aplicante/{aplicante_id}",response_model=Aplicante)
async def get_aplicante(aplicante_id: int):
    rpta = nuevo_aplicante.get_aplicante(aplicante_id)
    return rpta

@router.get("/get_aplicantes/")
async def get_aplicantes():
    rpta = nuevo_aplicante.get_aplicantes()
    return rpta

@router.put("/update_aplicante")
async def update_aplicante(aplicante: Aplicante):
    rpta = nuevo_aplicante.update_aplicante(aplicante)
    return rpta

@router.delete("/delete_aplicante/{aplicante_id}")
async def delete_aplicante(aplicante_id: int):
    rpta = nuevo_aplicante.delete_aplicante(aplicante_id)
    return rpta