from fastapi import APIRouter, HTTPException
from controllers.company_controller import *
from models.company_model import CompanyIn

router = APIRouter()

new_company = CompanyController()


@router.post("/create_company")
async def create_company(company: CompanyIn):
    response = new_company.create_company(company)
    return response


@router.get("/get_company/{company_id}",response_model=CompanyIn)
async def get_company(company_id: int):
    response = new_company.get_company(company_id)
    return response

@router.get("/get_companies/")
async def get_companies():
    response = new_company.get_companies()
    return response

@router.put("/update_company")
async def update_company(company: CompanyIn):
    response = new_company.update_company(company)
    return response

@router.delete("/delete_company/{company_id}")
async def delete_company(company_id: int):
    response = new_company.delete_company(company_id)
    return response