from sqlalchemy import Column, UUID, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from config.db_config import Base
from pydantic import BaseModel
from models.association_tables import attributesxuser
import uuid

class Attribute(Base):
    __tablename__ = "attributes"

    attributeid = Column(UUID, primary_key=True, index=True, default = uuid.uuid4)
    name = Column(String)

    # Define the relationship with users
    users = relationship("User", secondary=attributesxuser, back_populates="attributes")

class AttributeIn(BaseModel):
    attributeid: str
    name: str