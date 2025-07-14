from .user_model import *
from .province_model import *
from sqlmodel import SQLModel, create_engine, Session


DATABASE_URL = "sqlite:///./database.db"  # Change to your preferred DB URL

engine = create_engine(DATABASE_URL, echo=True)
session = Session(engine)

def create_db_and_tables():
    "Create the database and tables if they do not exist."
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    print("Database and tables created successfully.")
