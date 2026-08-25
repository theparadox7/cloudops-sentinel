from fastapi import FastAPI

app = FastAPI(
    title="CloudOps Sentinel",
    version="0.1.0",
)


@app.get("/health")
async def health_check():
    return {"status": "healthy"}