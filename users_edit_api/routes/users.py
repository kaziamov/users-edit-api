from fastapi import APIRouter

from users_edit_api.routes.schemas.user import UserCreateOrUpdate
from users_edit_api.database import get_connection

router = APIRouter()


@router.get('/users/')
async def get_users():
    query = """
        SELECT * FROM users;
    """
    async with get_connection() as conn:
        users = await conn.fetch(query)
    return users


@router.post('/users/')
async def create_user(args: UserCreateOrUpdate):
    query = """
        INSERT INTO users (name, password, "group")
        VALUES ($1, $2, $3)
        RETURNING id;
    """
    async with get_connection() as conn:
        users = await conn.fetch(
            query,
            args.name,
            args.password,
            args.group
        )
    return users


@router.patch('/users/{user_id}')
async def update_users(user_id: int, args: UserCreateOrUpdate):
    query = """
        UPDATE users SET name=$2, password=$3, "group"=$4
        WHERE users.id = $1;
    """
    async with get_connection() as conn:
        users = await conn.fetch(
            query,
            user_id,
            args.name,
            args.password,
            args.group,
        )
    return users


@router.delete('/users/{user_id}')
async def delete_users(user_id: int):
    query = """
        DELETE FROM users
        WHERE users.id = $1;
    """
    async with get_connection() as conn:
        users = await conn.fetch(
            query,
            user_id,
        )
    return users
