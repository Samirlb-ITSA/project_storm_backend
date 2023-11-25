from sqlalchemy import Column, Integer, String, UUID, ForeignKey
from sqlalchemy.orm import relationship
from config.db_config import Base
from pydantic import BaseModel
from models.association_tables import rolexuser
from typing import Optional
import uuid

class Role(Base):
    __tablename__ = "role"

    roleid = Column(UUID, primary_key=True, index=True, default = uuid.uuid4)
    name = Column(String)

    # Define the relationship with User
    users = relationship("User", secondary=rolexuser, back_populates="roles")

class RoleIn(BaseModel):
    roleid: Optional[str] = None
    name: str