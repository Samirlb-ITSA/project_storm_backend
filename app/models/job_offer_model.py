from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UUID, Boolean
from sqlalchemy.orm import relationship
from config.db_config import Base
from pydantic import BaseModel
from datetime import date
from typing import Optional
from models.company_model import Company
from datetime import datetime
import uuid

class JobOffer(Base):
    __tablename__ = "job_offers"

    offerid = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    workday = Column(String(100), nullable=False)
    status = Column(Boolean, nullable=False)
    creationdate = Column(DateTime, default=datetime.now)
    companyid = Column(UUID(as_uuid=True), ForeignKey(Company.companyid))

    # Define the relationship with Applicant
    applicants = relationship("Applicant", back_populates="job_offer")

class JobOfferIn(BaseModel):
    name: str
    workday: str
    status: bool
    companyid: str