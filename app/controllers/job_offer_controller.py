from fastapi import HTTPException
from config.db_config import get_db_connection
from models.job_offer_model import JobOffer, JobOfferIn
from models.company_model import Company
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload

class JobOfferController:
    def create_job_offer(self, job_offer: JobOfferIn):
        db = get_db_connection()
        try:
            db_job_offer = JobOffer(**job_offer.model_dump())
            print(db_job_offer)
            db.add(db_job_offer)
            db.commit()
            return {"resultado": "Oferta creada"}
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.close()

    def get_job_offer(self, job_offer_id: str):
        db = get_db_connection()
        try:
            job_offer = db.query(JobOffer).options(joinedload(JobOffer.applicants)).filter(JobOffer.offerid == job_offer_id).first()
            if job_offer is None:
                return {"resultado": "Oferta no encontrada"}
            
            job_offer = jsonable_encoder(job_offer)
            job_offer_dict = {
                "offerid": str(job_offer.offerid),
                "name": job_offer.name,
                "workday": job_offer.workday,
                "status": job_offer.status,
                "creationdate": job_offer.creationdate,
                "companyid": str(job_offer.companyid),
                "companyname": "Company Name",  # Set companyname from backend
                "companyaddress": "Company Address"  # Set companyaddress from backend
            }

            company = db.query(Company).filter(Company.companyid == job_offer["companyid"]).first()
            job_offer_dict["companyname"] = company.name
            job_offer_dict["companyaddress"] = company.address
            return job_offer_dict
        finally:
            db.close()

    def get_job_offers(self):
        db = get_db_connection()
        try:
            job_offers = db.query(JobOffer).options(joinedload(JobOffer.applicants)).all()
            if not job_offers:
                return {"resultado": "No se encontraron ofertas"}
            
            job_offers_list = []
            for job_offer in job_offers:
                company = db.query(Company).filter(Company.companyid == job_offer.companyid).first()
                if company:
                    companyname = company.name
                else:
                    companyname = "Company Name Not Found"
                
                job_offer_dict = {
                    "offerid": str(job_offer.offerid),
                    "name": job_offer.name,
                    "workday": job_offer.workday,
                    "status": job_offer.status,
                    "creationdate": job_offer.creationdate,
                    "companyid": str(job_offer.companyid),
                    "companyname": companyname,
                    "companyaddress": company.address  # You can fetch companyaddress similarly if needed
                }
                
                job_offers_list.append(job_offer_dict)
            
            return {"resultado": job_offers_list}
        finally:
            db.close()


    def update_job_offer(self, job_offer: JobOfferIn):
        db = get_db_connection()
        try:
            db_job_offer = db.query(JobOffer).filter(JobOffer.offerid == job_offer.offerid).first()
            if db_job_offer is None:
                raise HTTPException(status_code=404, detail="Oferta no encontrada")
            for var, value in vars(job_offer).items():
                setattr(db_job_offer, var, value) if value else None
            db.commit()
            return {"resultado": "Oferta actualizada"}
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.close()

    def delete_job_offer(self, job_offer_id: str):
        db = get_db_connection()
        try:
            db_job_offer = db.query(JobOffer).filter(JobOffer.offerid == job_offer_id).first()
            if db_job_offer is None:
                raise HTTPException(status_code=404, detail="Oferta no encontrada")
            db.delete(db_job_offer)
            db.commit()
            return {"resultado": "Oferta eliminada"}
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            db.close()