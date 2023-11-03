from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from datetime import date

Base = declarative_base()
class Oferta(Base):
    __tablename__ = "ofertaslaborales"

    idoferta = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    jornadalaboral = Column(String)
    estado = Column(Integer)
    fechacreacion = Column(DateTime)
    idempresa = Column(Integer, ForeignKey('empresa.idempresa'))

class OfertaIn(BaseModel):
    idoferta: int
    nombre: str
    jornadalaboral: str
    estado: int
    idempresa: int
