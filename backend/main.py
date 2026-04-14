from fastapi import FastAPI
from backend.routes.essay import router as essay_router

app = FastAPI(title="Essay Agent API")

app.include_router(essay_router, prefix="/api")

@app.get("/health")
def health():
    return {"status": "ok"}