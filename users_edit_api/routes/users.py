from fastapi import APIRouter

from users_edit_api.routes.schemas.user import User

router = APIRouter()


@router.get('/users/')
async def get_users(args: User):
    return []


@router.post('/users/<user_id>')
async def create_user(args: User):
    return {}


@router.post('/users/<user_id>')
async def update_users(args: User):
    return {}


@router.post('/users/<user_id>')
async def delete_users(args: User):
    return
