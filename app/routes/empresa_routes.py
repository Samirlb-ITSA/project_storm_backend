from fastapi import APIRouter, HTTPException
from controllers.empresa_controller import *
from models.empresa_model import Empresa

router = APIRouter()

nuevo_empresa = EmpresaController()


@router.post("/create_empresa")
async def create_empresa(empresa: Empresa):
    rpta = nuevo_empresa.create_empresa(empresa)
    return rpta


@router.get("/get_empresa/{empresa_id}",response_model=Empresa)
async def get_empresa(empresa_id: int):
    rpta = nuevo_empresa.get_empresa(empresa_id)
    return rpta

@router.get("/get_empresas/")
async def get_empresas():
    rpta = nuevo_empresa.get_empresas()
    return rpta

@router.put("/update_empresa")
async def update_empresa(empresa: Empresa):
    rpta = nuevo_empresa.update_empresa(empresa)
    return rpta

@router.delete("/delete_empresa/{empresa_id}")
async def delete_empresa(empresa_id: int):
    rpta = nuevo_empresa.delete_empresa(empresa_id)
    return rpta