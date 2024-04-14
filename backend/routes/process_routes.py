from fastapi import APIRouter, HTTPException
from queries.process_queries import get_all_processes, get_one_process_id, create_process, update_process, delete_process
from models.process_model import Process, UpdateProcess


process = APIRouter()


@process.get('/api/processes', tags=['Process'])
async def get_processes():
    processes = await get_all_processes()
    return processes


@process.get('/api/processes/{id}', response_model=Process, tags=['Process'])
async def get_process_by_id(id: str):
    process = await get_one_process_id(id)
    if process:
        return process
    raise HTTPException(400, "Could not find process")


@process.post('/api/processes', response_model=Process, tags=['Process'])
async def save_process(process: Process):

    response = await create_process(process.model_dump())

    if response:
        return response
    raise HTTPException(400, "Something went wrong")


@process.put('/api/processes/{id}', response_model=UpdateProcess, tags=['Process'])
async def put_process(id: str, process: UpdateProcess):
    response = await update_process(id, process)
    if response:
        return response

    raise HTTPException(404, "Process not found")


@process.delete('/api/processes/{id}', tags=['Process'])
async def remove_process(id: str):
    response = await delete_process(id)
    if response:
        return "Process deleted successfully"
    raise HTTPException(404, "Could not find the process")
