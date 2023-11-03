from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from datetime import date

Base = declarative_base()
class JobOffer(Base):
    __tablename__ = "joboffers"

    offerid = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    workday = Column(String)
    status = Column(Integer)
    creationdate = Column(DateTime)
    companyid = Column(Integer, ForeignKey('company.companyid'))

class JobOfferIn(BaseModel):
    offerid: int
    name: str
    workday: str
    status: int
    companyid: int