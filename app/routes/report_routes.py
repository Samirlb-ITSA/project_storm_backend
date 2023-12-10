# routes.py

from fastapi import FastAPI, Response
from fastapi.responses import FileResponse
from controllers.statistics_controller import StatisticsController
from controllers.auth_controller import AuthController
from controllers.report_controller import ReportController
from models.user_model import User
from fastapi import APIRouter, Depends

router = APIRouter()

auth_controller = AuthController()
statistics_controller = StatisticsController()
report_controller = ReportController()

@router.get("/report", response_class=FileResponse)
async def get_report(user: User = Depends(auth_controller.get_current_active_user)):
    user_stats = statistics_controller.get_user_statistics()
    job_stats = statistics_controller.get_job_statistics()
    company_stats = statistics_controller.get_company_statistics()

    report_file = report_controller.generate_report(user_stats, job_stats, company_stats)

    return FileResponse(report_file, media_type="application/pdf", filename="report.pdf")