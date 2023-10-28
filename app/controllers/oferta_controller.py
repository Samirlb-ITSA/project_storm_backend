import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.oferta_model import Oferta
from fastapi.encoders import jsonable_encoder

class OfertaController:
        
    def create_oferta(self, oferta: Oferta):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO `ofertaslaborales`(`nombre`, `jornadalaboral`, `estado`, `idempresa`) VALUES (%s, %s, %s, %s)", (oferta.nombre, oferta.jornadalaboral, oferta.estado, oferta.idempresa))
            conn.commit()
            conn.close()
            return {"resultado": "Oferta creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_oferta(self, oferta_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM ofertaslaborales WHERE idoferta = %s", (oferta_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'idoferta':int(result[0]),
                    'nombre':result[1],
                    'jornadalaboral':result[2],
                    'estado':int(result[3]),
                    'fechacreacion':result[4],
                    'idempresa':int(result[5])
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Oferta not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    def get_ofertas(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM ofertaslaborales")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'idoferta':data[0],
                    'nombre':data[1],
                    'jornadalaboral':data[2],
                    'estado':data[3],
                    'fechacreacion':data[4],
                    'idempresa':data[5]
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Oferta not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def update_oferta(self, oferta: Oferta):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""UPDATE ofertaslaborales 
                           SET idoferta = %s,
                           nombre = %s,
                           jornadalaboral = %s,
                           estado = %s,
                           fechacreacion = %s,
                           idempresa = %s,
                           WHERE idoferta = %s""", (oferta.idoferta,
                           oferta.nombre,oferta.jornadalaboral,oferta.estado,
                           oferta.fechacreacion,oferta.idempresa,oferta.idoferta,))
            conn.commit()
            conn.close()
            return {"resultado": "Oferta actualizado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def delete_oferta(self, oferta_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM ofertaslaborales WHERE idoferta = %s", (oferta_id,))
            conn.commit()
            conn.close()
            return {"resultado": "Oferta eliminado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
