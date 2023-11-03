from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Role(Base):
    __tablename__ = "role"

    roleid = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    # Define the relationship with User

class RoleIn(BaseModel):
    roleid: int
    name: str