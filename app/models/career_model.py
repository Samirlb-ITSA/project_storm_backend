from sqlalchemy import Column, UUID, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.association_tables import userxcareer
from pydantic import BaseModel
from config.db_config import Base
import uuid

class Career(Base):
    __tablename__ = "career"

    careerid = Column(UUID, primary_key=True, index=True, default = uuid.uuid4)
    name = Column(String)

    # Define the relationship with users
    users = relationship("User", secondary=userxcareer, back_populates="careers")

class CareerIn(BaseModel):
    careerid: str
    name: str