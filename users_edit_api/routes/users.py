from fastapi import APIRouter

from users_edit_api.routes.schemas.user import UserCreateOrUpdate
from users_edit_api.database import get_connection

router = APIRouter()


@router.get('/users/')
async def get_users():
    query = """
        SELECT * FROM users
    """
    with get_connection() as conn:
        users = await conn.fetchall(query)
        return users


@router.post('/users/')
async def create_user():
    return {}


@router.patch('/users/{user_id}')
async def update_users(user_id: int, args: UserCreateOrUpdate):
    return {}


@router.post('/users/{user_id}')
async def delete_users(user_id: int):
    return
