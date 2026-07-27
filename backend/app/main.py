from fastapi import FastAPI

from app.api.assets import router as assets_router

app = FastAPI(
    title="Cyber Defense Platform",
    version="0.1.0",
    description="AI-powered Cyber Defense Platform",
)


app.include_router(assets_router)


@app.get("/")
def root():
    return {
        "message": "Cyber Defense Platform API",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }