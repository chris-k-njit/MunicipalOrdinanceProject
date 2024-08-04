# app/main.py
from fastapi import FastAPI, Form, UploadFile, File
from app.data_processing import load_data, get_summary_statistics, search_ordinances
from app.llm_integration import generate_summary
import asyncio

app = FastAPI()

# Define a semaphore with a limit of 2 concurrent accesses
semaphore = asyncio.Semaphore(2)

# Global variable to store loaded data
dataframe = None

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    global dataframe
    async with semaphore:
        dataframe = pd.read_csv(file.file)
        summary = get_summary_statistics(dataframe)
        return summary.to_dict()

@app.post("/summarize/")
async def summarize_text(text: str):
    async with semaphore:
        summary = generate_summary(text)
        return {"summary": summary}

@app.post("/search/")
async def search_text(query: str = Form(...)):
    global dataframe
    if dataframe is not None:
        results = search_ordinances(dataframe, query)
        return results.to_dict(orient="records")
    else:
        return {"error": "No data loaded. Please upload a file first."}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}