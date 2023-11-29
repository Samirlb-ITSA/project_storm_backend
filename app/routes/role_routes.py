from fastapi import APIRouter, HTTPException, Depends
from controllers.role_controller import *
from controllers.auth_controller import AuthController
from models.user_model import RoleIn, User

router = APIRouter()

new_role = RoleController()
auth_controller = AuthController()

@router.post("/create_role")
async def create_role(role: RoleIn, current_user: User = Depends(auth_controller.get_current_active_user)):
    response = new_role.create_role(role)
    return response

@router.get("/get_role/{role_id}",response_model=RoleIn)
async def get_role(role_id: str, current_user: User = Depends(auth_controller.get_current_active_user)):
    response = new_role.get_role(role_id)
    return response

@router.get("/get_roles/")
async def get_roles(current_user: User = Depends(auth_controller.get_current_active_user)):
    response = new_role.get_roles()
    return response

@router.put("/update_role")
async def update_role(role: RoleIn, current_user: User = Depends(auth_controller.get_current_active_user)):
    response = new_role.update_role(role)
    return response

@router.delete("/delete_role/{role_id}")
async def delete_role(role_id: str, current_user: User = Depends(auth_controller.get_current_active_user)):
    response = new_role.delete_role(role_id)
    return response