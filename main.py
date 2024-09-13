from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust if necessary
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/data/{todo_id}")
async def read_data(todo_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'https://jsonplaceholder.typicode.com/todos/{todo_id}')
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Todo not found")
        data = response.json()
    return {"message": data['title']}
