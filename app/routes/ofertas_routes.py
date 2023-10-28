from fastapi import APIRouter, HTTPException
from controllers.oferta_controller import *
from models.oferta_model import Oferta

router = APIRouter()

nuevo_oferta = OfertaController()

@router.post("/create_oferta")
async def create_oferta(oferta: Oferta):
    rpta = nuevo_oferta.create_oferta(oferta)
    return rpta


@router.get("/get_oferta/{oferta_id}",response_model=Oferta)
async def get_oferta(oferta_id: int):
    rpta = nuevo_oferta.get_oferta(oferta_id)
    return rpta

@router.get("/get_ofertas/")
async def get_ofertas():
    rpta = nuevo_oferta.get_ofertas()
    return rpta

async def update_oferta(oferta: Oferta):
    rpta = nuevo_oferta.update_oferta(oferta)
    return rpta

@router.delete("/delete_oferta/{oferta_id}")
async def delete_oferta(oferta_id: int):
    rpta = nuevo_oferta.delete_oferta(oferta_id)
    return rpta