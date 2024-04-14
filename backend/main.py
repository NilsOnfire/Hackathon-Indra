from fastapi import FastAPI
from routes.user_routes import user
# from routes.process_routes import process
# from routes.stage_routes import stage
from fastapi.middleware.cors import CORSMiddleware
from decouple import config


app = FastAPI()

origins = [config('FRONTEND_URL')]
app.add_middleware(
    
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.title= "Talent Tracker"

@app.get("/",tags=['User'])
def welcome():
    return {"message": "Hello World"}

app.include_router(user)
# app.include_router(process)
# app.include_router(stage)
