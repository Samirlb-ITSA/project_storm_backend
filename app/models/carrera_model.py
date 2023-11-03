from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Carrera(Base):
    __tablename__ = "carrera"

    idcarrera = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)

class CarreraIn(BaseModel):
    idcarrera: int
    nombre: str
