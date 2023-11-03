from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

# Define the association table for User and Career
userxcareer = Table('userxcareer', Base.metadata,
    Column('userid', Integer, ForeignKey('users.userid')),
    Column('careerid', Integer, ForeignKey('career.careerid'))
)

class Career(Base):
    __tablename__ = "career"

    careerid = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    # Define the relationship with users
    users = relationship("User", secondary=userxcareer, back_populates="career")

class CareerIn(BaseModel):
    careerid: int
    name: str