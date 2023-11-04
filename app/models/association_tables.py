from sqlalchemy import Table, Column, Integer, ForeignKey
from config.db_config import Base

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