import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.rol_model import Rol
from fastapi.encoders import jsonable_encoder

class RolController:
        
    def create_rol(self, rol: Rol):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO `rol`(`idrol`, `nombre`) VALUES (%s, %s)", (rol.nombre))
            conn.commit()
            conn.close()
            return {"resultado": "Rol creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        
    def get_rol(self, rol_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM rol WHERE idrol = %s", (rol_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'idrol':int(result[0]),
                    'nombre':result[1]
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Rol not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    def get_rols(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM rol")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'idrol':data[0],
                    'nombre':data[1],

                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Rol not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
    def update_rol(self, rol: Rol):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE rol SET idrol = %s, nombre = %s WHERE idrol = %s", (rol.idrol,rol.nombre,rol.idrol,))
            conn.commit()
            conn.close()
            return {"resultado": "Rol actualizad"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def delete_rol(self, rol_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM rol WHERE idrol = %s", (rol_id,))
            conn.commit()
            conn.close()
            return {"resultado": "Rol eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    
       

##user_controller = UserController()