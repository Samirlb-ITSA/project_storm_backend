import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.user_model import UserIn, User
from models.role_model import Role
from models.career_model import Career
from models.attribute_model import Attribute

from models.login_model import Login
from fastapi.encoders import jsonable_encoder
from passlib.context import CryptContext
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import SQLAlchemyError

from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserController:
    def create_user(self, user: UserIn):
        db = get_db_connection()
        try:
            user.password = pwd_context.hash(user.password)
            
            db_user = User(**user.model_dump())
            db.add(db_user)
            db.commit()

            for role_id in user.role_ids:
                role = db.query(Role).get(role_id)
                if role is not None:
                    db_user.roles.append(role)

            for career_id in user.career_ids:
                career = db.query(Career).get(career_id)
                if career is not None:
                    db_user.careers.append(career)

            for attribute_id in user.attribute_ids:
                attribute = db.query(Attribute).get(attribute_id)
                if attribute is not None:
                    db_user.attributes.append(attribute)

            return {"result": "Usuario creado"}
        except SQLAlchemyError:
            db.rollback()
            return {"result": "Error al crear el usuario"}
        finally:
            db.close()

    def get_user(self, user_id: int):
        db = get_db_connection()
        try:
            user = db.query(User).options(joinedload(User.roles), joinedload(User.careers), joinedload(User.attributes)).filter(User.userid == user_id).first()
            if user is None:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")
            return jsonable_encoder(user)
        finally:
            db.close()

    def get_users(self):
        db = get_db_connection()
        try:
            users = db.query(User).options(joinedload(User.roles), joinedload(User.careers), joinedload(User.attributes)).all()
            if not users:
                raise HTTPException(status_code=404, detail="No se encontraron usuarios")
            return {"resultado": jsonable_encoder(users)}
        finally:
            db.close()

    def getUsersFromDb(self):
        db = get_db_connection()
        try:
            users = db.query(User).options(joinedload(User.roles), joinedload(User.careers), joinedload(User.attributes)).all()
            return users
        finally:
            db.close()

    def update_user(self, user: UserIn):
        db = get_db_connection()
        try:
            db_user = db.query(User).filter(User.userid == user.userid).first()
            if db_user is None:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")
            for var, value in vars(user).items():
                setattr(db_user, var, value) if value else None
            db.commit()
            return {"resultado": "Usuario actualizado"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al actualizar el usuario"}
        finally:
            db.close()

    def delete_user(self, user_id: int):
        db = get_db_connection()
        try:
            db_user = db.query(User).filter(User.userid == user_id).first()
            if db_user is None:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")
            db.delete(db_user)
            db.commit()
            return {"resultado": "Usuario eliminado"}
        except SQLAlchemyError:
            db.rollback()
            return {"resultado": "Error al eliminar el usuario"}
        finally:
            db.close()


##user_controller = UserController()