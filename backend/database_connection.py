from motor.motor_asyncio import AsyncIOMotorClient


def get_collection(model_name):
    uri = "mongodb+srv://delaossa777:Aloha123%2A@dbindra.wplghu5.mongodb.net/?retryWrites=true&w=majority&appName=dbIndra"

    client = AsyncIOMotorClient(uri,ssl=False)
    database = client.userDatabase
    collection = database[model_name]
    return collection
