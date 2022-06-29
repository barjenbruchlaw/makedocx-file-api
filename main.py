from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel

class Message(BaseModel):
    name: str
    datetime: datetime
    message: str

app = FastAPI()

@app.post('/message')
async def create_message(message: Message):
    return message