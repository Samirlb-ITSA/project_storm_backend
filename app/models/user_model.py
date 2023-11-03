from sqlalchemy import Column, Integer, String, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import List
from models.role_model import Role, RoleIn

Base = declarative_base()

# Define the association table for User and Role
rolexuser = Table('rolexuser', Base.metadata,
    Column('userid', Integer, ForeignKey('users.userid')),
    Column('roleid', Integer, ForeignKey('role.roleid'))
)

# Define the association table for User and Career
userxcareer = Table('userxcareer', Base.metadata,
    Column('userid', Integer, ForeignKey('users.userid')),
    Column('careerid', Integer, ForeignKey('career.careerid'))
)

# Define the association table for User and Attribute
attributesxuser = Table('attributesxuser', Base.metadata,
    Column('userid', Integer, ForeignKey('users.userid')),
    Column('attributeid', Integer, ForeignKey('attributes.attributeid'))
)

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
    applicants = relationship("Applicant", back_populates="users")

class UserIn(BaseModel):
    firstname: str
    lastname: str
    email: str
    cellphone: int
    address: str
    password: str
    status: int
    role_ids: List[int] = []
    career_ids: List[int] = []
    attribute_ids: List[int] = []