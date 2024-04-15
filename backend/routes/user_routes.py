
from fastapi import APIRouter, HTTPException
from queries.user_queries import get_all_users, create_user, get_one_user_email, get_one_user_id, delete_user, update_user, update_user_processes

from models.user_model import User, UpdateUser, UpdateUserProcesses


user = APIRouter()


@user.get('/api/users', tags=['User'])
async def get_users():
    users = await get_all_users()
    return users


@user.get('/api/users/{id}', response_model=User, tags=['User'])
async def get_user_by_id(id: str):
    user = await get_one_user_id(id)
    if user:
        return user
    raise HTTPException(400, "Could not find user id:{id}")


@user.post('/api/users', response_model=User, tags=['User'])
async def save_users(user: User):
    user_found = await get_one_user_email(user.email)

    if user_found:
        raise HTTPException(409, "User already exists ")

    response = await create_user(user.model_dump())

    if response:
        return response
    raise HTTPException(400, "Something went wrong")


@user.put('/api/users/{id}', response_model=UpdateUser, tags=['User'])
async def put_user(id: str, user: UpdateUser):
    response = await update_user(id, user)
    if response:
        return response

    raise HTTPException(404, "User with not found")


@user.delete('/api/users/{id}', tags=['User'])
async def remove_user(id: str):
    response = await delete_user(id)
    if response:
        return "User deleted successfully"
    raise HTTPException(404, "Could not find user id:{id}")


@user.put('/api/users/process/{email}', response_model=UpdateUserProcesses, tags=['User'])
async def put_user_process(email: str, userProcess: UpdateUserProcesses):
    response = await update_user_processes(email, userProcess)
    if response:
        return response

    raise HTTPException(404, "User with not found")
