from fastapi import FastAPI

app = FastAPI (title="FastAPI Docs RAG")

@app.get("/health")
def health():
    return {"status": "ok"}