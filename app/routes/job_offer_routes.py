from fastapi import APIRouter
from controllers.role_controller import *
from models.user_model import RoleIn

router = APIRouter()

new_role = RoleController()


@router.post("/create_role")
async def create_role_routes(role: RoleIn):
    response = new_role.create_role(role)
    return response

@router.get("/get_role/{role_id}",response_model=RoleIn)
async def get_role_routes(role_id: int):
    response = new_role.get_role(role_id)
    return response

@router.get("/get_roles/")
async def get_roles_routes():
    response = new_role.get_roles()
    return response

@router.put("/update_role")
async def update_role_routes(role: RoleIn):
    response = new_role.update_role(role)
    return response

@router.delete("/delete_role/{role_id}")
async def delete_role_routes(role_id: int):
    response = new_role.delete_role(role_id)
    return response