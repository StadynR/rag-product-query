import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.agents import RetrieverAgent, ResponderAgent

load_dotenv()

TOP_K = os.getenv('TOP_K')
PROMPT_FILE = os.getenv('PROMPT_FILE')

retriever = RetrieverAgent()

app = FastAPI()

# Input schema {user_id: str, query: str}
class QueryRequest(BaseModel):
    user_id: str
    query: str

@app.post("/query")
def handle_query(request: QueryRequest):
    # Data validation
    if not request.user_id.strip() or not request.query.strip():
        raise HTTPException(status_code=400, detail="Both 'user_id' and 'query' must be non-empty strings.")
    
    # Validate TOP_K
    top_k = 0
    if TOP_K:
        try:
            top_k = int(TOP_K)
            if top_k <= 0:
                raise ValueError("TOP_K must be a positive integer.")
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid TOP_K value. It must be a positive integer.")
    
    # Extract prompt from txt file as string
    prompt = ""
    if PROMPT_FILE:
        try:
            with open(PROMPT_FILE, 'r', encoding='utf-8') as file:
                prompt = file.read()
        except FileNotFoundError:
            raise HTTPException(status_code=500, detail=f"Prompt file '{PROMPT_FILE}' not found.")
    
    # Agent pipeline
    docs = retriever.retrieve(request.query, top_k)
    responder = ResponderAgent(prompt)
    answer = responder.generate(request.query, docs)

    return {
        "user_id": request.user_id,
        "answer": answer,
        "docs_used": docs
    }
