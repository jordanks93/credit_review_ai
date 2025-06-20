from fastapi import FastAPI, File, UploadFile, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from processor import process_document
from security import save_encrypted_file
import os

app = FastAPI()

# Enable CORS for front-end (lock down in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    filepath = os.path.join(UPLOAD_DIR, file.filename)
    contents = await file.read()
    enc_path = save_encrypted_file(filepath, contents)
    summary = process_document(enc_path)
    return JSONResponse(content={"summary": summary})