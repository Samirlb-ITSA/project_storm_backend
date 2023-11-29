from sqlalchemy import Column, Integer, String, DateTime, UUID, Boolean
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
import uuid

Base = declarative_base()

class Company(Base):
    __tablename__ = "company"

    companyid = Column(UUID, primary_key=True, index=True, default = uuid.uuid4)
    name = Column(String)
    email = Column(String)
    cellphone = Column(Integer)
    address = Column(String)
    nit = Column(Integer)
    status = Column(Boolean)
    creationdate = Column(DateTime)
    

class CompanyIn(BaseModel):
    companyid: Optional[str] = None
    name: str
    email: str
    cellphone: int
    address: str
    status: bool
    nit: int
    creationdate: datetime = datetime.now()
