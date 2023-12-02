from fastapi import HTTPException
from config.db_config import get_db_connection
from models.job_offer_model import JobOffer, JobOfferIn
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
            return jsonable_encoder(job_offer)
        finally:
            db.close()

    def get_job_offers(self):
        db = get_db_connection()
        try:
            job_offers = db.query(JobOffer).options(joinedload(JobOffer.applicants)).all()
            if not job_offers:
                return {"resultado": "No se encontraron ofertas"}
            return {"resultado": jsonable_encoder(job_offers)}
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