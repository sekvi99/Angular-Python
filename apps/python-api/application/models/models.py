import bcrypt
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """
    Class representing structure of users table in database.
    """
    
    __tablename__ = 'users' # Db table name
    
    id = Column(Integer, primary_key=True, index=True) # User id in database
    username = Column(String, unique=True, index=True) # User username in database
    e_mail = Column(String, unique=True, index=True)   # User e-mail in database
    password_hash = Column(String, nullable=False)     # User password hash in database
    connected_mail = Column(String, nullable=False)    # User supported e-mail not required
    
    def set_password(self, password: str) -> None:
        password = password.encode('utf-8')
        self.password_hash = bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password: str) -> bool:
        password = password.encode('utf-8')
        return bcrypt.checkpw(password, self.password_hash.encode('utf-8'))

class Session(Base):
    """
    Class representing structure of sessions table in database.
    """
    
    __tablename__ = 'sessions' # Db table name
    
    id = Column(Integer, primary_key=True, index=True) # Session id in database
    user_id = Column(Integer, ForeignKey('users.id'))  # User id related to given session
    token = Column(String)                             # Jwt token