from fastapi import FastAPI

app = FastAPI(title="QAOps-AI", version="0.1.0")


@app.get("/health")
def health():

    return {"status": "healthy"}


@app.get("/system")
def system():

    return {"platform": "QAOps-AI", "version": "0.1.0", "environment": "development"}
