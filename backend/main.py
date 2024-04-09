from fastapi import FastAPI
from routes.user import user


app = FastAPI()
app.title= "HackIndra"

@app.get("/",tags=['User'])
def welcome():
    return {"message": "Hello World"}

app.include_router(user)
