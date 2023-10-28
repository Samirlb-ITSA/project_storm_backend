import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.aplicante_model import Aplicante
from fastapi.encoders import jsonable_encoder

class AplicanteController:
        
    def create_aplicante(self, aplicante: Aplicante):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO `aplicantes`(`idoferta`, `idusuario`) VALUES (%s, %s)", (aplicante.idoferta, aplicante.idusuario))
            conn.commit()
            conn.close()
            return {"resultado": "Aplicante creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_aplicante(self, aplicante_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM aplicantes WHERE idaplicante = %s", (aplicante_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'idaplicante':int(result[0]),
                    'idoferta':int(result[1]),
                    'idusuario':int(result[2])
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Aplicante not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    def get_aplicantes(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM aplicante")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'idaplicante':data[0],
                    'nombre':data[1],
                    'correo':data[2],
                    'celular':data[3],
                    'direccion':data[4],
                    'nit':data[5]
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Aplicante not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def update_aplicante(self, aplicante: Aplicante):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""UPDATE aplicante 
                           SET idaplicante = %s,
                           nombre = %s,
                           correo = %s,
                           celular = %s,
                           direccion = %s,
                           nit = %s
                           WHERE idaplicante = %s""", (aplicante.idaplicante,
                           aplicante.nombre,aplicante.correo,aplicante.celular,
                           aplicante.direccion,aplicante.nit,aplicante.idaplicante,))
            conn.commit()
            conn.close()
            return {"resultado": "Aplicante actualizada"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def delete_aplicante(self, aplicante_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM aplicante WHERE idaplicante = %s", (aplicante_id,))
            conn.commit()
            conn.close()
            return {"resultado": "Aplicante eliminada"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

##aplicante_controller = AplicanteController()