from sqlalchemy.orm import joinedload
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from models.faculty_model import Faculty
from config.db_config import get_db_connection

class FacultyController:
    def get_faculties(self):
        db = get_db_connection()
        try:
            faculties = db.query(Faculty).all()
            if not faculties:
                return {"resultado": "No se encontraron facultades"}
            return {"resultado": jsonable_encoder(faculties)}
        finally:
            db.close()