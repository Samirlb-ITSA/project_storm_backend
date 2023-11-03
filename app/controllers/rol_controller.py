import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.rol_model import Rol, RolIn
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import SQLAlchemyError
from pydantic.main import model_dump

class RolController:
    def create_rol(rol: RolIn):
        db = get_db_connection()
        try:
            db_rol = Rol(**model_dump(rol))
            db.add(db_rol)
            db.commit()
            return {"resultado": "Rol creado"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al crear el rol"}
        finally:
            db.close()

    def get_rol(rol_id: int):
        db = get_db_connection()
        try:
            rol = db.query(Rol).filter(Rol.idrol == rol_id).first()
            if rol is None:
                raise HTTPException(status_code=404, detail="Rol not found")
            return jsonable_encoder(rol)
        finally:
            db.close()

    def get_roles():
        db = get_db_connection()
        try:
            roles = db.query(Rol).all()
            if not roles:
                raise HTTPException(status_code=404, detail="No roles found")
            return {"resultado": jsonable_encoder(roles)}
        finally:
            db.close()

    def update_rol(rol: RolIn):
        db = get_db_connection()
        try:
            db_rol = db.query(Rol).filter(Rol.idrol == rol.idrol).first()
            if db_rol is None:
                raise HTTPException(status_code=404, detail="Rol not found")
            for var, value in vars(rol).items():
                setattr(db_rol, var, value) if value else None
            db.commit()
            return {"resultado": "Rol actualizado"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al actualizar el rol"}
        finally:
            db.close()

    def delete_rol(rol_id: int):
        db = get_db_connection()
        try:
            db_rol = db.query(Rol).filter(Rol.idrol == rol_id).first()
            if db_rol is None:
                raise HTTPException(status_code=404, detail="Rol not found")
            db.delete(db_rol)
            db.commit()
            return {"resultado": "Rol eliminado"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al eliminar el rol"}
        finally:
            db.close()

##user_controller = UserController()