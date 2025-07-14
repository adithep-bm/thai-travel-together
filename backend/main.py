from fastapi import FastAPI
from . import models
from . import routers

app = FastAPI()
app.include_router(routers.router)

models.create_db_and_tables()

@app.get("/")
def read_root() -> dict:
    return {"Hello": "World"}


@app.get("/health")
def health_check() -> dict:
    """Health check endpoint for production monitoring."""
    return {"status": "healthy", "service": "flasx"}
