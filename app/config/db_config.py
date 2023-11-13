from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def get_db_connection():
    engine = create_engine("postgresql://fl0user:Q9o8AmCzcpNi@ep-tight-disk-29607304.us-east-2.aws.neon.fl0.io:5432/storm?sslmode=require&options=endpoint%3Dep-tight-disk-29607304")
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()