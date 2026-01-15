from typing import Annotated
import uvicorn
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename} 

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)