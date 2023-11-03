from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

# Define the association table for User and Attribute
attributesxuser = Table('attributesxuser', Base.metadata,
    Column('userid', Integer, ForeignKey('users.userid')),
    Column('attributeid', Integer, ForeignKey('attributes.attributeid'))
)

class Attribute(Base):
    __tablename__ = "attributes"

    attributeid = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    # Define the relationship with users
    users = relationship("User", secondary=attributesxuser, back_populates="attributes")

class AttributeIn(BaseModel):
    attributeid: int
    name: str