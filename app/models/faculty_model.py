from sqlalchemy import Column, String, UUID
from sqlalchemy.orm import relationship
from config.db_config import Base
import uuid
from pydantic import BaseModel

class Faculty(Base):
    __tablename__ = "faculties"

    facultyid = Column(UUID, primary_key=True, index=True, default = uuid.uuid4)
    name = Column(String)

    # Define the relationship with Career
    careers = relationship("Career", back_populates="faculty")

class FacultyIn(BaseModel):
    facultyid: str
    name: str
