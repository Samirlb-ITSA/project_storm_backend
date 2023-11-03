from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Applicant(Base):
    __tablename__ = "applicants"

    applicantid = Column(Integer, primary_key=True, index=True)
    offerid = Column(Integer)
    userid = Column(Integer, ForeignKey('users.userid'))

    # Define the relationship with User
    user = relationship("User", back_populates="applicants")

class ApplicantIn(BaseModel):
    applicantid: int
    offerid: int
    userid: int