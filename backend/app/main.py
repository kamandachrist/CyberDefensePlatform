from fastapi import FastAPI

app = FastAPI(
    title="Cyber Defense Platform",
    version="0.1.0",
    description="AI-powered Cyber Defense Platform"
)


@app.get("/")
def root():
    return {
        "message": "Cyber Defense Platform API",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }