from controllers.statistics_controller import StatisticsController
from controllers.auth_controller import AuthController
from fastapi import APIRouter, Depends
from models.user_model import RoleIn, User

router = APIRouter()

statistics_controller = StatisticsController()
auth_controller = AuthController()

@router.get("/statistics")
async def get_statistics(user: User = Depends(auth_controller.get_current_active_user)):
    response = statistics_controller.getStatistics()
    return response