import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.empresa_model import Empresa
from fastapi.encoders import jsonable_encoder

class EmpresaController:
        
    def create_empresa(self, empresa: Empresa):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO `empresa`(`nombre`, `correo`, `celular`, `direccion`, `nit`) VALUES (%s, %s, %s, %s, %s)", (empresa.nombre, empresa.correo, empresa.celular, empresa.direccion,  empresa.nit))
            conn.commit()
            conn.close()
            return {"resultado": "Empresa creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_empresa(self, empresa_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM empresa WHERE idempresa = %s", (empresa_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'idempresa':int(result[0]),
                    'nombre':result[1],
                    'correo':result[2],
                    'celular':int(result[3]),
                    'direccion':result[4],
                    'nit':int(result[5])
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Empresa not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    def get_empresas(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM empresa")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'idempresa':data[0],
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
                raise HTTPException(status_code=404, detail="Empresa not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def update_empresa(self, empresa: Empresa):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""UPDATE empresa 
                           SET idempresa = %s,
                           nombre = %s,
                           correo = %s,
                           celular = %s,
                           direccion = %s,
                           nit = %s
                           WHERE idempresa = %s""", (empresa.idempresa,
                           empresa.nombre,empresa.correo,empresa.celular,
                           empresa.direccion,empresa.nit,empresa.idempresa,))
            conn.commit()
            conn.close()
            return {"resultado": "Empresa actualizada"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def delete_empresa(self, empresa_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM empresa WHERE idempresa = %s", (empresa_id,))
            conn.commit()
            conn.close()
            return {"resultado": "Empresa eliminada"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

##empresa_controller = EmpresaController()