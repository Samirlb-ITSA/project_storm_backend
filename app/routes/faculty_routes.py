from controllers.faculty_controller import FacultyController
from fastapi import APIRouter, Depends
from models.user_model import User
from controllers.auth_controller import AuthController

faculty_controller = FacultyController()
router = APIRouter()
auth_controller = AuthController()

@router.get("/get_faculties/")
async def get_faculties(current_user: User = Depends(auth_controller.get_current_active_user)):
    response = faculty_controller.get_faculties()
    return response