# main.py
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from pdf_utils import extract_text_from_pdf
from openai_utils import ask_openai_question
from typing import List

app = FastAPI()
book_content = {}
conversation_history = []

@app.post("/upload-book/")
async def upload_book(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")
    try:
        # Extract text from PDF
        text = extract_text_from_pdf(file.file)
        book_content['text'] = text
        conversation_history.clear()  # Clear any previous history
        return {"message": "Book uploaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ask-question/")
async def ask_question(question: str):
    if 'text' not in book_content:
        raise HTTPException(status_code=400, detail="No book uploaded.")
    # Call the OpenAI API utility
    answer = ask_openai_question(book_content['text'], question, conversation_history)
    conversation_history.append({"question": question, "answer": answer})
    return JSONResponse(content={"answer": answer})

@app.post("/replace-book/")
async def replace_book():
    book_content.clear()
    conversation_history.clear()
    return {"message": "Book content and history cleared. Ready for new upload."}
