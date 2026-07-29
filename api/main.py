from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from orchestration.platform_bootstrap import PlatformBootstrap

from portal.api.chat_api import router as chat_router
from portal.api.dashboard_api import router as dashboard_router
from portal.api.health_api import router as health_router


app = FastAPI(
    title="QAOps-AI Enterprise Portal",
    description="Enterprise AI Quality Engineering Platform",
    version="1.1.0",
)

# CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():

    print("\n====================================")
    print("Starting QAOps-AI Enterprise Portal")
    print("====================================\n")

    PlatformBootstrap.initialize()

    print("\n====================================")
    print("QAOps-AI Enterprise Portal Ready")
    print("====================================\n")


# Routers

app.include_router(
    chat_router,
    tags=["Chat"],
)

app.include_router(
    dashboard_router,
    tags=["Dashboard"],
)

app.include_router(
    health_router,
    tags=["Health"],
)


@app.get(
    "/",
    tags=["System"],
)
def root():

    return {
        "platform": "QAOps-AI Enterprise Portal",
        "version": "1.1.0",
        "status": "running",
    }


@app.get(
    "/system",
    tags=["System"],
)
def system():

    return {
        "platform": "QAOps-AI Enterprise",
        "portal": "active",
        "api": "active",
        "status": "healthy",
    }
