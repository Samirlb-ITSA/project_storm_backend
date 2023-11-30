from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UUID, Boolean
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from datetime import date
from typing import Optional
from models.company_model import Company
from datetime import datetime
import uuid

Base = declarative_base()
class JobOffer(Base):
    __tablename__ = "job_offers"

    offerid = Column(UUID, primary_key=True, index=True, default = uuid.uuid4)
    name = Column(String)
    workday = Column(String)
    status = Column(Boolean)
    creationdate = Column(DateTime, default=datetime.now)
    companyid = Column(UUID, ForeignKey(Company.companyid))

class JobOfferIn(BaseModel):
    name: str
    workday: str
    status: bool
    companyid: str