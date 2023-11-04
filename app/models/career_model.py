from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.association_tables import userxcareer
from pydantic import BaseModel
from config.db_config import Base

class Career(Base):
    __tablename__ = "career"

    careerid = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    # Define the relationship with users
    users = relationship("User", secondary=userxcareer, back_populates="careers")

class CareerIn(BaseModel):
    careerid: int
    name: str