from sqlalchemy import Table, Column, UUID, ForeignKey
from config.db_config import Base

# Define the association table for User and Role
rolexuser = Table('role_user', Base.metadata,
    Column('userid', UUID, ForeignKey('users.userid')),
    Column('roleid', UUID, ForeignKey('role.roleid'))
)

# Define the association table for User and Career
userxcareer = Table('user_career', Base.metadata,
    Column('userid', UUID, ForeignKey('users.userid')),
    Column('careerid', UUID, ForeignKey('career.careerid'))
)

# Define the association table for User and Attribute
attributesxuser = Table('attributes_user', Base.metadata,
    Column('userid', UUID, ForeignKey('users.userid')),
    Column('attributeid', UUID, ForeignKey('attributes.attributeid'))
)