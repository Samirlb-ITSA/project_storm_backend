from sqlalchemy import Column, UUID, ForeignKey
from sqlalchemy.orm import relationship
from config.db_config import Base
from pydantic import BaseModel
import uuid
class Applicant(Base):
    __tablename__ = "applicants"

    applicantid = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    offerid = Column(UUID(as_uuid=True), ForeignKey('job_offers.offerid'))
    userid = Column(UUID(as_uuid=True), ForeignKey('users.userid'))

    # Define the relationship with JobOffer
    job_offer = relationship("JobOffer", back_populates="applicants")

    # Define the relationship with User
    # user = relationship("User", back_populates="applicants")

class ApplicantIn(BaseModel):
    offerid: str
    userid: str