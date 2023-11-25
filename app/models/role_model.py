from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from config.db_config import Base
from pydantic import BaseModel
from models.association_tables import rolexuser
from typing import Optional

class Role(Base):
    __tablename__ = "role"

    roleid = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    # Define the relationship with User
    users = relationship("User", secondary=rolexuser, back_populates="roles")

class RoleIn(BaseModel):
    roleid: Optional[int] = None
    name: str