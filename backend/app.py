from fastapi import FastAPI
from chatbot import get_answer

app = FastAPI(title="INDUS AI")

@app.get("/")
def home():
    return {"message": "Welcome to INDUS AI"}

@app.get("/chat")
def chat(query: str):
    answer = get_answer(query)
    return {"response": answer}
