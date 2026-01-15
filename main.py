import uvicorn
import pandas as pd
from models import Terorists
from service import CsvFile

from fastapi import FastAPI, File, UploadFile, Form

app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    if not file:
        return {"detail": "No file provided"}
    if file.filename and not file.filename.endswith("csv"):
        return {"detail": "Invalid CSV file"}
    top_terorist = CsvFile(f'{file.filename}').top_terorist().to_dict(orient="dict")
    
    return { 
        "count":len(top_terorist),
         "top": [top_terorist] 
         }


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)