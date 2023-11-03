from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Empresa(Base):
    __tablename__ = "empresa"

    idempresa = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    correo = Column(String)
    celular = Column(Integer)
    direccion = Column(String)
    nit = Column(Integer)

class EmpresaIn(BaseModel):
    idempresa: int
    nombre: str
    correo: str
    celular: int
    direccion: str
    nit: int