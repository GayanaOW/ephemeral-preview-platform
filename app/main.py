from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "status": "healthy",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "environment": os.getenv("ENVIRONMENT", "local")
    }

@app.get("/healthz")
def healthcheck():
    return {"status": "ok"}