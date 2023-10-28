from pydantic import BaseModel

class Oferta(BaseModel):
    idoferta: int
    nombre: str
    jornadalaboral: str
    estado: int
    fechacreacion: str
    idempresa: int
