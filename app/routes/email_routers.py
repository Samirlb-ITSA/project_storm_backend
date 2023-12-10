# routers/email_router.py

from fastapi import APIRouter
from controllers.user_controller import send_email

router = APIRouter()

@router.post("/send_email/")
async def send_email_route(to_email: str, subject: str, password: str):
    return await send_email(to_email, subject)