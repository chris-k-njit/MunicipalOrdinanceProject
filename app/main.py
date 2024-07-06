# app/main.py
from fastapi import FastAPI, UploadFile, File
from app.data_processing.py import load_data, get_summary_statistics

app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    data = load_data(file.file)
    summary = get_summary_statistics(data)
    return summary.to_dict()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
