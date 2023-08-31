import logging
from datetime import timedelta

import bcrypt
from fastapi import FastAPI, HTTPException, Path, Query
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from application.consts.consts import (ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM,
                                       DB_POSTGRES_URL, SECRET_KEY)
from application.helpers.helpers import create_access_token
from application.models.models import Base, User
from application.responses.user_response import UserResponse

app = FastAPI()

logging.info('Creating database')
engine = create_engine(DB_POSTGRES_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Endpoints for handling user management

@app.post('/api/create-user', response_model=UserResponse, tags=['User'])
async def create_user(
    username: str = Query(..., description='Username of the user to create.'),
    email: str = Query(..., description='Email of the user to create.'),
    password: str = Query(..., description='Password for the user.'),
    connected_mail: str = Query(None, description='Optional connected email.'),
    ):
    
    # Hash the password before storing it in the database
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    # Create a new user instance
    new_user = User(username=username, e_mail=email, password_hash=password_hash, connected_mail=connected_mail)
    
    # Add the user to the session and commit to the database
    db = SessionLocal()
    db.add(new_user)
    db.commit()
    db.close()
    
    return UserResponse(
        message='User created successfully',
        username=username,
        email=email
    )
    
@app.get('/api/get-user/{user_id}', tags=['User'])
async def get_user(
    user_id: int = Path(..., description='ID of the user to retrieve')
    ):
    
    # Retrieve the user by ID
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    db.close()

    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    
    return user
    
@app.put('/api/modify-user/{user_id}', tags=['User'])
async def modify_user(
    user_id: int = Path(..., description='ID of the user to modify'),
    new_username: str = None,
    new_email: str = None,
    new_connected_mail: str = None
):
    
    # Retrieve the user by ID
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        db.close()
        raise HTTPException(status_code=404, detail='User not found')

    # Update user information if new values are provided
    if new_username:
        user.username = new_username
    if new_email:
        user.e_mail = new_email
    if new_connected_mail:
        user.connected_mail = new_connected_mail
    
    # Commit the changes to the database
    db.commit()
    db.close()

    return db.query(User).filter(User.id == user_id).first()
    
@app.delete('/api/delete-user/{user_id}', response_model=UserResponse, tags=['User'])
async def delete_user(
    user_id: int = Path(..., description='ID of the user to delete')
    ):
    # Retrieve the user by ID
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        db.close()
        raise HTTPException(status_code=404, detail='User not found')

    # Delete the user from the database
    db.delete(user)
    db.commit()
    db.close()

    return UserResponse(
        message='User deleted successfully',
        username=None,
        email=None
    )
    
# Endpoints for handling user session

@app.post('/api/authenticate', tags=['User login'])
async def login(
    username: str,
    password: str):
    # Retrieve the user by username
    db = SessionLocal()
    db_user = db.query(User).filter(User.username == username).first()
    
    db.close()

    if db_user is None or not db_user.check_password(password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = await create_access_token({"sub": db_user.username}, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM)
    
    return {"access_token": access_token, "token_type": "bearer"}
