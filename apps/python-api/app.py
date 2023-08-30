from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from application.models.models import Base, User, Session
import logging
from application.consts.consts import DB_POSTGRES_URL

app = FastAPI()

logging.info('Creating database')
engine = create_engine(DB_POSTGRES_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)