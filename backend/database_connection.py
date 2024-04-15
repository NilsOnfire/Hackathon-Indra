from motor.motor_asyncio import AsyncIOMotorClient


def get_collection(model_name):
    uri = "mongodb+srv://delaossa777:Aloha123%2A@dbindra.wplghu5.mongodb.net/?retryWrites=true&w=majority&appName=dbIndra"

    client = AsyncIOMotorClient(uri)
    database = client.userDatabase
    collection = database[model_name,ssl=False]
    return collection
