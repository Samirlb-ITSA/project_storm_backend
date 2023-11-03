import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.aplicante_model import Aplicante, AplicanteIn
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import SQLAlchemyError

class AplicanteController:
    def create_aplicante(aplicante: AplicanteIn):
        db = get_db_connection()
        try:
            db_aplicante = Aplicante(aplicante.model_dump())
            db.add(db_aplicante)
            db.commit()
            return {"resultado": "Aplicante creado"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al crear el aplicante"}
        finally:
            db.close()

    def get_aplicante(aplicante_id: int):
        db = get_db_connection()
        try:
            aplicante = db.query(Aplicante).options(joinedload(Aplicante.user)).filter(Aplicante.idaplicante == aplicante_id).first()
            if aplicante is None:
                raise HTTPException(status_code=404, detail="Aplicante not found")
            return jsonable_encoder(aplicante)
        finally:
            db.close()

    def get_aplicantes():
        db = get_db_connection()
        try:
            aplicantes = db.query(Aplicante).options(joinedload(Aplicante.user)).all()
            if not aplicantes:
                raise HTTPException(status_code=404, detail="No aplicantes found")
            return {"resultado": jsonable_encoder(aplicantes)}
        finally:
            db.close()

    def update_aplicante(aplicante: AplicanteIn):
        db = get_db_connection()
        try:
            db_aplicante = db.query(Aplicante).filter(Aplicante.idaplicante == aplicante.idaplicante).first()
            if db_aplicante is None:
                raise HTTPException(status_code=404, detail="Aplicante not found")
            for var, value in vars(aplicante).items():
                setattr(db_aplicante, var, value) if value else None
            db.commit()
            return {"resultado": "Aplicante actualizado"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al actualizar el aplicante"}
        finally:
            db.close()

    def delete_aplicante(aplicante_id: int):
        db = get_db_connection()
        try:
            db_aplicante = db.query(Aplicante).filter(Aplicante.idaplicante == aplicante_id).first()
            if db_aplicante is None:
                raise HTTPException(status_code=404, detail="Aplicante not found")
            db.delete(db_aplicante)
            db.commit()
            return {"resultado": "Aplicante eliminada"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al eliminar el aplicante"}
        finally:
            db.close()

##aplicante_controller = AplicanteController()