from pydantic import BaseModel

class Carrera(BaseModel):
    idcarrera: int
    nombre: str
