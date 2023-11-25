from sqlalchemy import Column, UUID, ForeignKey
from sqlalchemy.orm import relationship
from config.db_config import Base
from pydantic import BaseModel
import uuid
class Applicant(Base):
    __tablename__ = "applicants"

    applicantid = Column(UUID, primary_key=True, index=True, default = uuid.uuid4)
    offerid = Column(UUID, ForeignKey('joboffers.offerid'))
    userid = Column(UUID, ForeignKey('users.userid'))

    # Define the relationship with User
    # user = relationship("User", back_populates="applicants")

class ApplicantIn(BaseModel):
    applicantid: str
    offerid: str
    userid: str