import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.oferta_model import Oferta, OfertaIn
from fastapi.encoders import jsonable_encode
from sqlalchemy.exc import SQLAlchemyError
from pydantic.main import model_dump

class OfertaController:
    def create_oferta(oferta: OfertaIn):
        db = get_db_connection()
        try:
            db_oferta = Oferta(**model_dump(oferta))
            db.add(db_oferta)
            db.commit()
            return {"resultado": "Oferta creada"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al crear la oferta"}
        finally:
            db.close()

    def get_oferta(oferta_id: int):
        db = get_db_connection()
        try:
            oferta = db.query(Oferta).filter(Oferta.idoferta == oferta_id).first()
            if oferta is None:
                raise HTTPException(status_code=404, detail="Oferta not found")
            return jsonable_encode(oferta)
        finally:
            db.close()

    def get_ofertas():
        db = get_db_connection()
        try:
            ofertas = db.query(Oferta).all()
            if not ofertas:
                raise HTTPException(status_code=404, detail="No ofertas found")
            return {"resultado": jsonable_encode(ofertas)}
        finally:
            db.close()

    def update_oferta(oferta: OfertaIn):
        db = get_db_connection()
        try:
            db_oferta = db.query(Oferta).filter(Oferta.idoferta == oferta.idoferta).first()
            if db_oferta is None:
                raise HTTPException(status_code=404, detail="Oferta not found")
            for var, value in vars(oferta).items():
                setattr(db_oferta, var, value) if value else None
            db.commit()
            return {"resultado": "Oferta actualizada"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al actualizar la oferta"}
        finally:
            db.close()

    def delete_oferta(oferta_id: int):
        db = get_db_connection()
        try:
            db_oferta = db.query(Oferta).filter(Oferta.idoferta == oferta_id).first()
            if db_oferta is None:
                raise HTTPException(status_code=404, detail="Oferta not found")
            db.delete(db_oferta)
            db.commit()
            return {"resultado": "Oferta eliminada"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al eliminar la oferta"}
        finally:
            db.close()
