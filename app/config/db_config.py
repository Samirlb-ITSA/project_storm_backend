from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_db_connection():
    engine = create_engine("mysql+mysqlconnector://root:@localhost/storm")
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()