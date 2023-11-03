import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.empresa_model import Empresa, EmpresaIn
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import SQLAlchemyError
from pydantic.main import model_dump

class EmpresaController:
    def create_empresa(empresa: EmpresaIn):
        db = get_db_connection()
        try:
            db_empresa = Empresa(**model_dump(empresa))
            db.add(db_empresa)
            db.commit()
            return {"resultado": "Empresa creada"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al crear la empresa"}
        finally:
            db.close()

    def get_empresa(empresa_id: int):
        db = get_db_connection()
        try:
            empresa = db.query(Empresa).filter(Empresa.idempresa == empresa_id).first()
            if empresa is None:
                raise HTTPException(status_code=404, detail="Empresa not found")
            return jsonable_encoder(empresa)
        finally:
            db.close()

    def get_empresas():
        db = get_db_connection()
        try:
            empresas = db.query(Empresa).all()
            if not empresas:
                raise HTTPException(status_code=404, detail="No empresas found")
            return {"resultado": jsonable_encoder(empresas)}
        finally:
            db.close()

    def update_empresa(empresa: EmpresaIn):
        db = get_db_connection()
        try:
            db_empresa = db.query(Empresa).filter(Empresa.idempresa == empresa.idempresa).first()
            if db_empresa is None:
                raise HTTPException(status_code=404, detail="Empresa not found")
            for var, value in vars(empresa).items():
                setattr(db_empresa, var, value) if value else None
            db.commit()
            return {"resultado": "Empresa actualizada"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al actualizar la empresa"}
        finally:
            db.close()

    def delete_empresa(empresa_id: int):
        db = get_db_connection()
        try:
            db_empresa = db.query(Empresa).filter(Empresa.idempresa == empresa_id).first()
            if db_empresa is None:
                raise HTTPException(status_code=404, detail="Empresa not found")
            db.delete(db_empresa)
            db.commit()
            return {"resultado": "Empresa eliminada"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al eliminar la empresa"}
        finally:
            db.close()

##empresa_controller = EmpresaController()