from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from config.db_config import Base
from pydantic import BaseModel
class Applicant(Base):
    __tablename__ = "applicants"

    applicantid = Column(Integer, primary_key=True, index=True)
    offerid = Column(Integer)
    userid = Column(Integer, ForeignKey('users.userid'))

    # Define the relationship with User
    # user = relationship("User", back_populates="applicants")

class ApplicantIn(BaseModel):
    applicantid: int
    offerid: int
    userid: int