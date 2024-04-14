from database_connection import get_collection
from models.process_model import Process
from bson import ObjectId

collection = get_collection('processes')


async def get_one_process_id(id):
    process = await collection.find_one({'_id': ObjectId(id)})
    return process


async def get_all_processes():
    processes = []
    async for document in collection.find({}):
        # Crear una instancia de Process con los datos del documento
        process = Process(**document)
        processes.append(process)
    return processes


async def create_process(process):
    new_process = await collection.insert_one(process)
    created_process = await collection.find_one({'_id': new_process.inserted_id})
    return created_process


async def update_process(id: str, data):
    process = {k: v for k, v in data.dict().items() if v is not None}
    await collection.update_one({'_id': ObjectId(id)}, {'$set': process})
    document = await collection.find_one({'_id': ObjectId(id)})
    return document


async def delete_process(id: str):
    await collection.delete_one({'_id': ObjectId(id)})
    return True
