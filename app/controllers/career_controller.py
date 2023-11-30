from fastapi import HTTPException
from config.db_config import get_db_connection
from models.career_model import Career, CareerIn
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload

class CareerController:
    def create_career(self, career: CareerIn):
        db = get_db_connection()
        try:
            db_career = Career(**career.model_dump())
            db.add(db_career)
            db.commit()
            return {"resultado": "Carrera creada"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al crear la carrera"}
        finally:
            db.close()

    def get_career(self, career_id: str):
        db = get_db_connection()
        try:
            career = db.query(Career).options(joinedload(Career.faculty)).filter(Career.careerid == career_id).first()
            if career is None:
                raise HTTPException(status_code=404, detail="Carrera no encontrada")
            return jsonable_encoder(career)
        finally:
            db.close()

    def get_careers(self):
        db = get_db_connection()
        try:
            careers = db.query(Career).options(joinedload(Career.faculty)).all()
            if not careers:
                raise HTTPException(status_code=404, detail="No se encontraron carreras")
            return {"resultado": jsonable_encoder(careers)}
        finally:
            db.close()

    def update_career(self, career: CareerIn):
        db = get_db_connection()
        try:
            db_career = db.query(Career).filter(Career.careerid == career.careerid).first()
            if db_career is None:
                raise HTTPException(status_code=404, detail="Carrera no encontrada")
            for var, value in vars(career).items():
                setattr(db_career, var, value) if value else None
            db.commit()
            return {"resultado": "Carrera actualizada"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al actualizar la carrera"}
        finally:
            db.close()

    def delete_career(self, career_id: str):
        db = get_db_connection()
        try:
            db_career = db.query(Career).filter(Career.careerid == career_id).first()
            if db_career is None:
                raise HTTPException(status_code=404, detail="Carrera no encontrada")
            db.delete(db_career)
            db.commit()
            return {"resultado": "Carrera eliminada"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al eliminar la carrera"}
        finally:
            db.close()

##career_controller = CareerController()