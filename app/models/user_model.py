from sqlalchemy import Column, Integer, String, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship
from config.db_config import Base
from pydantic import BaseModel
from typing import List
from models.role_model import Role, RoleIn
from datetime import datetime
from models.association_tables import rolexuser, userxcareer, attributesxuser

class User(Base):
    __tablename__ = "users"

    userid = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)
    cellphone = Column(Integer)
    address = Column(String)
    password = Column(String)
    status = Column(Integer)
    creationdate = Column(DateTime)

    # Define the relationship with Role
    roles = relationship("Role", secondary=rolexuser, back_populates="users")

    # Define the relationship with Career
    careers = relationship("Career", secondary=userxcareer, back_populates="users")

    # Define the relationship with Attribute
    attributes = relationship("Attribute", secondary=attributesxuser, back_populates="users")

    # Define the relationship with Applicant
    # applicants = relationship("Applicant", back_populates="users")

class UserIn(BaseModel):
    firstname: str
    lastname: str
    email: str
    cellphone: int
    address: str
    password: str
    status: int
    creationdate: datetime = datetime.now()
    roles: List[int] = []
    careers: List[int] = []
    # attributes: List[int] = []