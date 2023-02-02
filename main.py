from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.post("/word_count")
async def word_count(text: str):
    return {"word_count": len(text.split())}
