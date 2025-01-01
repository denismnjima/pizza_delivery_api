from fastapi import APIRouter,status
from fastapi.exceptions import HTTPException
from database import engine,Session
from models import User
from schemas import SignUpModel
from werkzeug.security import generate_password_hash
auth_routes = APIRouter(
    prefix= '/auth',
    tags = ['auth']
)
session = Session(bind = engine)

@auth_routes.get('/')
async def say_hi():
    return {'message': 'hello world'}

@auth_routes.post('/signup',status_code=status.HTTP_201_CREATED )
async def signup(user:SignUpModel):

    db_email = session.query(User).filter(User.email == user.email).first()
    if db_email is not None:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail= 'Email is already registered'
            )
    
    db_username = session.query(User).filter(User.username == user.username).first()
    if db_username is not None:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail= 'Username is already registered'
            )
    
    new_user = User(
        username = user.username,
        email = user.db_email,
        password = generate_password_hash(user.password),
        is_active = user.is_active,
        is_staff = user.is_staff
    )

    session.add(new_user)
    session.commit()