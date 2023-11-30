from fastapi import APIRouter, HTTPException, Depends

from controllers.job_offer_controller import JobOfferController
from controllers.auth_controller import AuthController

from models.job_offer_model import JobOfferIn, JobOffer

router = APIRouter()

new_job_offer = JobOfferController()
auth_controller = AuthController()

@router.post("/create_job_offer")
async def create_job_offer_routes(job_offer: JobOfferIn, current_user: JobOffer = Depends(auth_controller.get_current_active_user)):
    response = new_job_offer.create_job_offer(job_offer)
    return response

@router.get("/get_offer/{job_offer_id}",response_model=JobOfferIn)
async def get_job_offer_routes(job_offer_id: str, current_user: JobOffer = Depends(auth_controller.get_current_active_user)):
    response = new_job_offer.get_job_offer(job_offer_id)
    return response

@router.get("/get_job_offers/")
async def get_job_offers(current_user: JobOffer = Depends(auth_controller.get_current_active_user)):
    response = new_job_offer.get_job_offers()
    return response

@router.put("/update_job_offer")
async def update_job_offer_routes(job_offer: JobOfferIn, current_user: JobOffer = Depends(auth_controller.get_current_active_user)):
    response = new_job_offer.update_job_offer(job_offer)
    return response

@router.delete("/delete_job_offer/{job_offer_id}")
async def delete_job_offer_routes(job_offer_id: str, current_user: JobOffer = Depends(auth_controller.get_current_active_user)):
    response = new_job_offer.delete_job_offer(job_offer_id)
    return response