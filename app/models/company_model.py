from sqlalchemy import Column, Integer, String, DateTime, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

Base = declarative_base()

class Company(Base):
    __tablename__ = "company"

    companyid = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    cellphone = Column(Integer)
    address = Column(String)
    nit = Column(Integer)
    status = Column(Integer)
    creationdate = Column(DateTime)
    

class CompanyIn(BaseModel):
    #companyid: Optional[int] = None
    name: str
    email: str
    cellphone: int
    address: str
    nit: int
    creationdate: datetime = datetime.now()
    #creationdate: datetime = datetime.now()