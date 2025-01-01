from fastapi import APIRouter

auth_routes = APIRouter(
    prefix= '/auth',
    tags = ['auth']
)

@auth_routes.get('/')
async def say_hi():
    return {'message': 'hello world'}