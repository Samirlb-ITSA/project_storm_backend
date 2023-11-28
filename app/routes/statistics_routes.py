from controllers.statistics_controller import StatisticsController
from controllers.auth_controller import AuthController
from fastapi import APIRouter, Depends
from models.user_model import RoleIn, User

router = APIRouter()

auth_controller = AuthController()

@router.get("/statistics/user")
async def get_user_statistics(user: User = Depends(auth_controller.get_current_active_user)):
    statistics_controller = StatisticsController()
    return statistics_controller.get_user_statistics()

@router.get("/statistics/job")
async def get_job_statistics(user: User = Depends(auth_controller.get_current_active_user)):
    statistics_controller = StatisticsController()
    return statistics_controller.get_job_statistics()

@router.get("/statistics/company")
async def get_company_statistics(user: User = Depends(auth_controller.get_current_active_user)):
    statistics_controller = StatisticsController()
    return statistics_controller.get_company_statistics()