from fastapi import APIRouter

order_routes = APIRouter(
    prefix= '/orders',
    tags = ['orders']
)

@order_routes.get('/')
async def get_orders():
    return {'message': 'hello world'}