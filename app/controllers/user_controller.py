import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.user_model import User
from models.login_model import Login
from fastapi.encoders import jsonable_encoder
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserController:
        
    def create_user(self, user: User):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            contraseña = pwd_context.hash(user.contraseña)
            cursor.execute("INSERT INTO `usuarios`(`nombre`, `apellido`, `correo`, `celular`, `direccion`, `contraseña`, `estado`) VALUES (%s, %s, %s, %s, %s, %s, %s)", (user.nombre, user.apellido, user.correo, user.celular, user.direccion, contraseña , user.estado))
            conn.commit()
            postid=cursor.lastrowid
            cursor.execute("INSERT INTO `rolxusuario`(`idusuario`, `idrol`) VALUES (%s, %s)", (postid, 1))
            conn.commit()
            conn.close()
            return {"resultado": "Usuario creado"}
        except mysql.connector.Error as err:
            print("Error creating user: ", err)
            conn.rollback()
        finally:
            conn.close()
        

    def get_user(self, user_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE idusuario = %s", (user_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'idusuario':int(result[0]),
                    'nombre':result[1],
                    'apellido':result[2],
                    'correo':result[3],
                    'celular':int(result[4]),
                    'direccion':result[5],
                    'contraseña':result[6],
                    'estado':int(result[7]),
                    'fechacreacion':result[8]
            }
            
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="User not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    def get_users(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'idusuario':data[0],
                    'nombre':data[1],
                    'apellido':data[2],
                    'correo':data[3],
                    'celular':data[4],
                    'direccion':data[5],
                    'contraseña':data[6],
                    'estado':data[7],
                    'fechacreacion':data[8]
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="User not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def getUsersFromDb(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios")
            result = cursor.fetchall()
            users = []
            for data in result:
                user = User()
                user.idusuario = data[0]
                user.nombre = data[1]
                user.apellido = data[2]
                user.correo = data[3]
                user.celular = data[4]
                user.direccion = data[5]
                user.contraseña = data[6]
                user.estado = data[7]
                user.fechacreacion = data[8]
                users.append(user)
            return users

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
            

    def update_user(self, user: User):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""UPDATE usuarios 
                           SET nombre = %s,
                           apellido = %s,
                           correo = %s,
                           celular = %s,
                           direccion = %s,
                           contraseña = %s,
                           estado = %s
                           WHERE idusuario = %s""", (user.nombre,user.apellido,user.correo,
                           user.celular,user.direccion,user.contraseña,
                           user.estado,user.idusuario))
            conn.commit()
            conn.close()
            return {"resultado": "User actualizado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def delete_user(self, user_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM usuarios WHERE idusuario = %s", (user_id,))
            conn.commit()
            conn.close()
            return {"resultado": "User eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def authenticate_user(self, login: Login):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE correo = %s AND contraseña = %s", (login.email, login.password))
            result = cursor.fetchone()
            if result:
                user_data = {
                    'idusuario': int(result[0]),
                    'nombre': result[1],
                    'apellido': result[2],
                    'correo': result[3],
                    'celular': int(result[4]),
                    'direccion': result[5],
                    'estado': int(result[7]),
                    'fechacreacion': result[8]
                }
                return user_data
            else:
                raise HTTPException(status_code=401, detail="Credenciales incorrectas")
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail="Error de servidor")
        finally:
            conn.close()

##user_controller = UserController()