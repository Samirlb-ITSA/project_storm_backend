from fastapi import HTTPException
from config.db_config import get_db_connection
from models.applicant_model import Applicant, ApplicantIn
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload

class ApplicantController:
    def create_applicant(self, applicant: ApplicantIn):
        db = get_db_connection()
        try:
            db_applicant = Applicant(**applicant.model_dump())
            db.add(db_applicant)
            db.commit()
            return {"resultado": "Aplicante creado"}
        except SQLAlchemyError as error:
            print(str(error.orig))
            db.rollback()
            return HTTPException(status_code=500, resultado="Error al crear el aplicante")
        finally:
            db.close()

    def get_applicant(self, applicant_id: str):
        db = get_db_connection()
        try:
            applicant = db.query(Applicant).options(joinedload(Applicant.job_offer)).filter(Applicant.applicantid == applicant_id).first()
            if applicant is None:
                raise HTTPException(status_code=404, detail="Aplicante not found")
            return jsonable_encoder(applicant)
        finally:
            db.close()

    def get_applicants(self):
        db = get_db_connection()
        try:
            applicants = db.query(Applicant).options(joinedload(Applicant.job_offer)).all()
            if not applicants:
                raise HTTPException(status_code=404, detail="No aplicantes found")
            return {"resultado": jsonable_encoder(applicants)}
        finally:
            db.close()

    def update_applicant(self, applicant: ApplicantIn):
        db = get_db_connection()
        try:
            db_applicant = db.query(Applicant).filter(Applicant.applicantid == applicant.applicantid).first()
            if db_applicant is None:
                raise HTTPException(status_code=404, detail="Aplicante not found")
            for var, value in vars(applicant).items():
                setattr(db_applicant, var, value) if value else None
            db.commit()
            return {"resultado": "Aplicante actualizado"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al actualizar el aplicante"}
        finally:
            db.close()

    def delete_applicant(self, applicant_id: str):
        db = get_db_connection()
        try:
            db_applicant = db.query(Applicant).filter(Applicant.applicantid == applicant_id).first()
            if db_applicant is None:
                raise HTTPException(status_code=404, detail="Aplicante not found")
            db.delete(db_applicant)
            db.commit()
            return {"resultado": "Aplicante eliminada"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al eliminar el aplicante"}
        finally:
            db.close()

##applicant_controller = ApplicantController()