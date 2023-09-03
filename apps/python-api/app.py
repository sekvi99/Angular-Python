import logging
from datetime import timedelta

import bcrypt
from fastapi import Depends, FastAPI, HTTPException, Path, Query
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from application.consts.consts import (ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM,
                                       DB_POSTGRES_URL, SECRET_KEY)
from application.helpers.api_key import authorize
from application.helpers.helpers import create_access_token
from application.models.models import Base, User
from application.responses.user_create_response import UserCreateRequest
from application.responses.user_login_response import LoginRequest
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
    user_data: UserCreateRequest,
    auth: bool = Depends(authorize)
):
    db = SessionLocal()
    
    # Check if a user with the provided email or username already exists
    existing_user = db.query(User).filter(
        (User.email == user_data.email) | (User.username == user_data.username)
    ).first()
    
    if existing_user:
        raise HTTPException(status_code=422, detail="User with the same email or username already exists")
    
    # Hash the password before storing it in the database
    password_hash = bcrypt.hashpw(user_data.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    # Create a new user instance
    new_user = User(username=user_data.username, email=user_data.email, 
                    password_hash=password_hash, connected_mail=user_data.connected_mail)
    
    # Add the user to the session and commit to the database
    db.add(new_user)
    db.commit()
    db.close()
    
    return UserResponse(
        message='User created successfully',
        username=user_data.username,
        email=user_data.email
    )
    
@app.get('/api/get-user/{user_id}', tags=['User'])
async def get_user_by_id(
    auth: bool = Depends(authorize),
    user_id: int = Path(..., description='ID of the user to retrieve')
    ):
    
    # Retrieve the user by ID
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    db.close()

    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    
    return user

@app.get('/api/user', tags=['User'])
async def get_user_by_username(
    auth: bool = Depends(authorize),
    username: str = Query(..., description='Username of user to extract')
    ):
    
    # Retrieve the user by username
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    db.close()

    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    
    return user

@app.put('/api/modify-user/{user_id}', tags=['User'])
async def modify_user(
    auth: bool = Depends(authorize),
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
        user.email = new_email
    if new_connected_mail:
        user.connected_mail = new_connected_mail
    
    # Commit the changes to the database
    db.commit()
    db.close()

    return db.query(User).filter(User.id == user_id).first()
    
@app.delete('/api/delete-user/{user_id}', response_model=UserResponse, tags=['User'])
async def delete_user(
    auth: bool = Depends(authorize),
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
    login_request: LoginRequest
):
    # Retrieve the user by username
    db = SessionLocal()
    db_user = db.query(User).filter(User.username == login_request.username).first()
    
    if db_user is None or not bcrypt.checkpw(login_request.password.encode('utf-8'), db_user.password_hash.encode('utf-8')):
        db.close()
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Generate an access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = await create_access_token({"sub": db_user.username}, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM)
    
    db.close()
    
    return {"access_token": access_token, "token_type": "bearer"}
