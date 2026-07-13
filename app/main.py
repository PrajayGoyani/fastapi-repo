from fastapi import FastAPI
from app.database import init_db
from app.routers import items

init_db()

app = FastAPI(
    title="FastAPI Learning App",
    description="FastAPI with PostgreSQL integration using SQLAlchemy",
    version="1.0.0"
)

# Include routers
app.include_router(items.router)

@app.get("/")
def read_root():
    # print(help(FastAPI.include_router))
    return {"message": "Welcome to the FastAPI Postgres Integration API!"}
