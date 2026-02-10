import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure DATABASE_URL from environment variable
DATABASE_URL = os.getenv('DATABASE_URL') or 'sqlite:///./app.db'

# Create engine
engine = create_engine(DATABASE_URL)

# Create SessionLocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define Base
Base = declarative_base()

# Create get_db function that yields database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()