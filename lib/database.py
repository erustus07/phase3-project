from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models.model_1 import Base

DATABASE_URL = "sqlite:///library.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def initialize_database():
    Base.metadata.create_all(engine)
