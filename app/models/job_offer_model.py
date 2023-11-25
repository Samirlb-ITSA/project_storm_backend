from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UUID
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from datetime import date
import uuid

Base = declarative_base()
class JobOffer(Base):
    __tablename__ = "joboffers"

    offerid = Column(UUID, primary_key=True, index=True, default = uuid.uuid4)
    name = Column(String)
    workday = Column(String)
    status = Column(Integer)
    creationdate = Column(DateTime)
    companyid = Column(Integer, ForeignKey('company.companyid'))

class JobOfferIn(BaseModel):
    offerid: str
    name: str
    workday: str
    status: int
    companyid: int