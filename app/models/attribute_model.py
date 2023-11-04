from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from config.db_config import Base
from pydantic import BaseModel
from models.association_tables import attributesxuser

class Attribute(Base):
    __tablename__ = "attributes"

    attributeid = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    # Define the relationship with users
    users = relationship("User", secondary=attributesxuser, back_populates="attributes")

class AttributeIn(BaseModel):
    attributeid: int
    name: str