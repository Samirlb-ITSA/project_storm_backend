import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.user_model import UserIn, User
from models.rol_model import Role
from models.login_model import Login
from fastapi.encoders import jsonable_encoder
from passlib.context import CryptContext
from sqlalchemy.orm import joinedload

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
from sqlalchemy.exc import SQLAlchemyError
from pydantic.main import model_dump

class UserController:
    def create_user(user: UserIn):
        db = get_db_connection()
        try:
            db_user = User(**model_dump(user))
            db.add(db_user)
            db.commit()

            for role_id in user.role_ids:
                role = db.query(Rol).get(role_id)
                if role is not None:
                    db_user.roles.append(role)

            for carrera_id in user.carrera_ids:
                carrera = db.query(Carrera).get(carrera_id)
                if carrera is not None:
                    db_user.carreras.append(carrera)

            for atributo_id in user.atributo_ids:
                atributo = db.query(Atributo).get(atributo_id)
                if atributo is not None:
                    db_user.atributos.append(atributo)

            db.commit()

            return {"resultado": "Usuario creado"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al crear el usuario"}
        finally:
            db.close()

    def get_user(user_id: int):
        db = get_db_connection()
        try:
            user = db.query(User).options(joinedload(User.roles), joinedload(User.carreras), joinedload(User.atributos), joinedload(User.aplicantes)).filter(User.idusuario == user_id).first()
            if user is None:
                raise HTTPException(status_code=404, detail="User not found")
            return jsonable_encoder(user)
        finally:
            db.close()

    def get_users():
        db = get_db_connection()
        try:
            users = db.query(User).options(joinedload(User.roles), joinedload(User.carreras), joinedload(User.atributos), joinedload(User.aplicantes)).all()
            if not users:
                raise HTTPException(status_code=404, detail="No users found")
            return {"resultado": jsonable_encoder(users)}
        finally:
            db.close()

    def update_user(user: UserIn):
        db = get_db_connection()
        try:
            db_user = db.query(User).filter(User.idusuario == user.idusuario).first()
            if db_user is None:
                raise HTTPException(status_code=404, detail="User not found")
            for var, value in vars(user).items():
                setattr(db_user, var, value) if value else None
            db.commit()
            return {"resultado": "User actualizado"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al actualizar el user"}
        finally:
            db.close()

    def delete_user(user_id: int):
        db = get_db_connection()
        try:
            db_user = db.query(User).filter(User.idusuario == user_id).first()
            if db_user is None:
                raise HTTPException(status_code=404, detail="User not found")
            db.delete(db_user)
            db.commit()
            return {"resultado": "User eliminado"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al eliminar el user"}
        finally:
            db.close()


##user_controller = UserController()