from fastapi import FastAPI, UploadFile, File
from typing import List
from Rag_pipline import Rag

app = FastAPI(title='AI-PDFChatBot',version='1.0')
rag = Rag()

@app.post("/upload")
async def upload(files: List[UploadFile] = File(...)):
    pdf_bytes = [await f.read() for f in files]
    chunks = rag.ingest(pdf_bytes)
    return {"status": "ok", "chunks_added": chunks}

@app.get("/chat")
async def chat(q: str, session_id: str):
    answer = rag.chat(q, session_id)
    return {"answer": answer}