# app/main.py
from fastapi import FastAPI, UploadFile, File
from app.data_processing import load_data, get_summary_statistics
from app.llm_integration import generate_summary
import asyncio

app = FastAPI()

# Define a semaphore with a limit of 2 concurrent accesses
semaphore = asyncio.Semaphore(2)

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    data = load_data(file.file)
    summary = get_summary_statistics(data)
    return summary.to_dict()

@app.post("/summarize/")
async def summarize_text(text: str):
    summary = generate_summary(text)
    return {"summary": summary}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
