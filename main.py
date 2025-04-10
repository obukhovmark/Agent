from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

@app.get("/")
def root():
    return {"message": "LuxAi Concierge is running"}
