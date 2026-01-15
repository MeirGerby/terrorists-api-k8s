from typing import Annotated
import uvicorn
from fastapi import FastAPI, File, UploadFile
import pandas as pd

app = FastAPI()

 
@app.post("/multipart/form-data")
async def create_upload_file(file: UploadFile = File(...)):
    data = pd.read_csv(file.file)
    df = pd.DataFrame(data)
    print(df)
    return True

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)