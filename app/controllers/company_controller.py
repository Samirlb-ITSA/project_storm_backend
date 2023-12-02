from fastapi import HTTPException
from config.db_config import get_db_connection
from models.company_model import Company, CompanyIn
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import SQLAlchemyError

class CompanyController:
    def create_company(self, company: CompanyIn):
        db = get_db_connection()
        try:
            db_company = Company(**company.model_dump())
            db.add(db_company)
            db.commit()
            return {"resultado": "Empresa creada"}
        except SQLAlchemyError as err:
            db.rollback()
            print(f"Error de MySQL: {err}")
            return {"resultado": "Error al crear la empresa"}
            
        finally:
            db.close()

    def get_company(self, company_id: str):
        db = get_db_connection()
        try:
            company = db.query(Company).filter(Company.companyid == company_id).first()
            if company is None:
                raise HTTPException(status_code=404, detail="Empresa no encontrada")
            return jsonable_encoder(company)
        finally:
            db.close()

    def get_companies(self):
        db = get_db_connection()
        try:
            companies = db.query(Company).all()
            if not companies:
                raise HTTPException(status_code=404, detail="No se encontraron empresas")
            return {"resultado": jsonable_encoder(companies)}
        finally:
            db.close()

    def update_company(self, company: CompanyIn):
        db = get_db_connection()
        try:
            db_company = db.query(Company).filter(Company.companyid == company.companyid).first()
            if db_company is None:
                raise HTTPException(status_code=404, detail="Empresa no encontrada")
            for var, value in vars(company).items():
                setattr(db_company, var, value) if value else None
            db.commit()
            return {"resultado": "Empresa actualizada"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al actualizar la empresa"}
        finally:
            db.close()

    def delete_company(self, company_id: str):
        db = get_db_connection()
        try:
            db_company = db.query(Company).filter(Company.companyid == company_id).first()
            if db_company is None:
                raise HTTPException(status_code=404, detail="Empresa no encontrada")
            db.delete(db_company)
            db.commit()
            return {"resultado": "Empresa eliminada"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al eliminar la empresa"}
        finally:
            db.close()

##company_controller = CompanyController()