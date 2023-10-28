import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.carrera_model import Carrera
from fastapi.encoders import jsonable_encoder

class CarreraController:
        
    def create_carrera(self, carrera: Carrera):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO `carrera`(`nombre`) VALUES (%s)", (carrera.nombre))
            conn.commit()
            conn.close()
            return {"resultado": "Carrera creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def get_carrera(self, carrera_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM carrera WHERE idcarrera = %s", (carrera_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 

            content={
                    'idcarrera':int(result[0]),
                    'nombre':result[1],
            }
            payload.append(content)

            json_data = jsonable_encoder(content)
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Carrera not found")

        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def get_carreras(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM carrera")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'idcarrera':data[0],
                    'nombre':data[1],

                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Carrera not found")  
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def update_carrera(self, carrera: Carrera):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE carrera SET idcarrera = %s, nombre = %s WHERE idcarrera = %s", (carrera.idcarrera,carrera.nombre,carrera.idcarrera,))
            conn.commit()
            conn.close()
            return {"resultado": "Carrera actualizada"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def delete_carrera(self, carrera_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM carrera WHERE idcarrera = %s", (carrera_id,))
            conn.commit()
            conn.close()
            return {"resultado": "Carrera eliminada"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

##user_controller = UserController()