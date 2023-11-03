from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Company(Base):
    __tablename__ = "company"

    companyid = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    cellphone = Column(Integer)
    address = Column(String)
    nit = Column(Integer)

class CompanyIn(BaseModel):
    companyid: int
    name: str
    email: str
    cellphone: int
    address: str
    nit: int