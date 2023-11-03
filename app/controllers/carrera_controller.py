from fastapi import HTTPException
from config.db_config import get_db_connection
from models.carrera_model import Carrera, CarreraIn
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload

class CarreraController:
    def create_carrera(carrera: CarreraIn):
        db = get_db_connection()
        try:
            db_carrera = Carrera(carrera.model_dump())
            db.add(db_carrera)
            db.commit()
            return {"resultado": "Carrera creada"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al crear la carrera"}
        finally:
            db.close()

    def get_carrera(carrera_id: int):
        db = get_db_connection()
        try:
            carrera = db.query(Carrera).options(joinedload(Carrera.users)).filter(Carrera.idcarrera == carrera_id).first()
            if carrera is None:
                raise HTTPException(status_code=404, detail="Carrera not found")
            return jsonable_encoder(carrera)
        finally:
            db.close()

    def get_carreras():
        db = get_db_connection()
        try:
            carreras = db.query(Carrera).options(joinedload(Carrera.users)).all()
            if not carreras:
                raise HTTPException(status_code=404, detail="No carreras found")
            return {"resultado": jsonable_encoder(carreras)}
        finally:
            db.close()

    def update_carrera(carrera: CarreraIn):
        db = get_db_connection()
        try:
            db_carrera = db.query(Carrera).filter(Carrera.idcarrera == carrera.idcarrera).first()
            if db_carrera is None:
                raise HTTPException(status_code=404, detail="Carrera not found")
            for var, value in vars(carrera).items():
                setattr(db_carrera, var, value) if value else None
            db.commit()
            return {"resultado": "Carrera actualizada"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al actualizar la carrera"}
        finally:
            db.close()

    def delete_carrera(carrera_id: int):
        db = get_db_connection()
        try:
            db_carrera = db.query(Carrera).filter(Carrera.idcarrera == carrera_id).first()
            if db_carrera is None:
                raise HTTPException(status_code=404, detail="Carrera not found")
            db.delete(db_carrera)
            db.commit()
            return {"resultado": "Carrera eliminada"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al eliminar la carrera"}
        finally:
            db.close()

##user_controller = UserController()