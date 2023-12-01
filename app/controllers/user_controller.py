from fastapi import HTTPException, UploadFile, File
import pandas as pd
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
from datetime import datetime

from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserController:
    def create_user(self, user: UserIn):
        db = get_db_connection()
        try:
            # Crear copias de roles y carreras
            roles_in = user.roles
            careers_in = user.careers

            # Vaciar roles y carreras en UserIn
            user.roles = []
            user.careers = []

            # Crear un nuevo objeto User
            user.password = pwd_context.hash(user.password)
            db_user = User(**user.model_dump())

            # Asignar los roles y carreras
            for rol in roles_in:
                role = db.query(Role).get(rol.roleid)
                if role is not None:
                    db_user.roles.append(role)

            for career in careers_in:
                career = db.query(Career).get(career.careerid)
                if career is not None:
                    db_user.careers.append(career)

            db.add(db_user)
            db.commit()
            return {"result": "Usuario creado"}
        except SQLAlchemyError as error:
            db.rollback()
            print(error)
            return {"result": "Error al crear el usuario"}
        finally:
            db.close()

    def get_user(self, user_id: str):
        db = get_db_connection()
        try:
            user = db.query(User).options(joinedload(User.roles), joinedload(User.careers), joinedload(User.attributes)).filter(User.userid == user_id).first()
            if user is None:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")
            user_dict = dict(user.__dict__)
            user_dict.pop('_sa_instance_state', None)
            return jsonable_encoder(user_dict)
        finally:
            db.close()

    def get_users(self):
        db = get_db_connection()
        try:
            users = db.query(User).options(joinedload(User.roles), joinedload(User.careers), joinedload(User.attributes)).all()
            if not users:
                raise HTTPException(status_code=404, detail="No se encontraron usuarios")
            users_dict = [dict(user.__dict__) for user in users]
            for user_dict in users_dict:
                user_dict.pop('_sa_instance_state', None)
            return {"resultado": jsonable_encoder(users_dict)}
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

    def delete_user(self, user_id: str):
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

    def import_users(self, file: UploadFile = File(...)):
        df = pd.read_excel(file.file)
        users = df.to_dict(orient='records')

        db = get_db_connection()
        created_users = []
        failed_users = []
        try:
            for i, user in enumerate(users, start=1):
                try:
                    user['password'] = pwd_context.hash(str(user['password']))

                    # Create the User object without the 'roles' and 'careers' fields
                    db_user = User(firstname=user['firstname'], lastname=user['lastname'], email=user['email'],
                                cellphone=user['cellphone'], address=user['address'], password=user['password'],
                                status=user['status'], creationdate=datetime.utcnow())


                    role = db.query(Role).get(user['roles'])
                    if role is not None:
                        db_user.roles.append(role)

                    career = db.query(Career).get(user['careers'])
                    if career is not None:
                        db_user.careers.append(career)

                    db.add(db_user)
                    db.commit()
                    created_users.append({"email": user['email'], "position": i})
                except SQLAlchemyError as error:
                    print(error)
                    db.rollback()
                    failed_users.append({"email": user['email'], "position": i})
        finally:
            db.close()
        return {
            "result": "Upload completed",
            "users_created": created_users,
            "users_failed": failed_users
        }


##user_controller = UserController()