from fastapi import HTTPException
from config.db_config import get_db_connection
from models.user_model import Role, RoleIn
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload

class RoleController:
    def create_role(self, role: RoleIn):
        db = get_db_connection()
        try:
            db_role = Role(**role.model_dump())
            db.add(db_role)
            db.commit()
            return {"resultado": "Rol creado"}
        except SQLAlchemyError  as err:
            db.rollback()
            print("Error de MySQL: {err}")
            return {"resultado": "Error al crear el rol"}
        finally:
            db.close()

    def get_role(self, role_id: str):
        db = get_db_connection()
        try:
            role = db.query(Role).options(joinedload(Role.users)).filter(Role.roleid == role_id).first()
            if role is None:
                raise HTTPException(status_code=404, detail="Rol no encontrado")
            return jsonable_encoder(role)
        finally:
            db.close()

    def get_roles(self):
        db = get_db_connection()
        try:
            roles = db.query(Role).options(joinedload(Role.users)).all()
            if not roles:
                raise HTTPException(status_code=404, detail="No se encontraron roles")
            return {"resultado": jsonable_encoder(roles)}
        except SQLAlchemyError  as err:
            db.rollback()
            print("Error de MySQL: {err}")
        finally:
            db.close()

    def update_role(self, role: RoleIn):
        db = get_db_connection()
        try:
            db_role = db.query(Role).filter(Role.roleid == role.roleid).first()
            if db_role is None:
                raise HTTPException(status_code=404, detail="Rol no encontrado")
            for var, value in vars(role).items():
                setattr(db_role, var, value) if value else None
            db.commit()
            return {"resultado": "Rol actualizado"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al actualizar el rol"}
        finally:
            db.close()

    def delete_role(self, role_id: str):
        db = get_db_connection()
        try:
            db_role = db.query(Role).filter(Role.roleid == role_id).first()
            if db_role is None:
                raise HTTPException(status_code=404, detail="Rol no encontrado")
            db.delete(db_role)
            db.commit()
            return {"resultado": "Rol eliminado"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al eliminar el rol"}
        finally:
            db.close()

##role_controller = RoleController()