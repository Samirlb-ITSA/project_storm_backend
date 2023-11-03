from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Aplicante(Base):
    __tablename__ = "aplicantes"

    idaplicante = Column(Integer, primary_key=True, index=True)
    idoferta = Column(Integer)
    idusuario = Column(Integer, ForeignKey('usuarios.id'))

class AplicanteIn(BaseModel):
    idoferta: int
    idusuario: int