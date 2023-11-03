from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "usuarios"

    idusuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    apellido = Column(String)
    correo = Column(String)
    celular = Column(String)
    direccion = Column(String)
    contraseña = Column(String)
    estado = Column(Integer)
    fechacreacion = Column(String)


class UserIn(BaseModel):
    idusuario: int = None
    nombre: str
    apellido: str
    correo: str
    celular: str
    direccion: str
    contraseña: str
    estado: int
    fechacreacion:str = None
