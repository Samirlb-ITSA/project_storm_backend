from sqlalchemy import Column, String, UUID, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from config.db_config import Base
from models.association_tables import userxcareer
from pydantic import BaseModel
from models.faculty_model import Faculty, FacultyIn
import uuid

class Career(Base):
    __tablename__ = "career"

    careerid = Column(UUID, primary_key=True, index=True, default = uuid.uuid4)
    name = Column(String)
    status = Column(Boolean)
    facultyid = Column(UUID, ForeignKey('faculties.facultyid'))

    # Define the relationship with Faculty
    faculty = relationship("Faculty", back_populates="careers")

    # Define the relationship with User
    users = relationship("User", secondary=userxcareer, back_populates="careers")

class CareerIn(BaseModel):
    name: str
    status: bool
    facultyid: str