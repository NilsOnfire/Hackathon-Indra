from database_connection import get_collection
from models.user_model import User
from bson import ObjectId

collection = get_collection('users')

async def get_one_user_id(id):
    user = await collection.find_one({'_id': ObjectId(id)})
    return user


async def get_one_user_email(email):
    user = await collection.find_one({'email': email})
    return user


async def get_all_users():
    users = []
    async for document in collection.find({}):
        user = User(**document)  # Crear una instancia de User con los datos del documento
        users.append(user)
    return users


async def  create_user(user):
    new_user = await collection.insert_one(user)
    created_user = await collection.find_one({'_id':new_user.inserted_id})
    return created_user


async def  update_user(id: str,data):
    user = {k:v for k,v in data.dict().items() if v is not None}
    await collection.update_one({'_id':ObjectId(id)}, {'$set':user})
    document = await collection.find_one({'_id':ObjectId(id)})
    return document


async def  delete_user(id:str):
    await collection.delete_one({'_id':ObjectId(id)})
    return True

