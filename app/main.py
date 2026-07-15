from fastapi import FastAPI
from app.database import init_db
from app.routers import auth, items, ingest, results

# init_db() # deprecated

app = FastAPI(
    title="FastAPI Learning App",
    description="FastAPI with PostgreSQL integration using SQLAlchemy",
    version="1.0.0"
)


# Include routers
app.include_router(items.router) # DML Endpoint

# user's auth + other endpoints
app.include_router(auth.router)

# Data pipeline enpoints
app.include_router(ingest.router) 
app.include_router(results.router)

@app.get("/")
def read_root():
    # print(help(FastAPI.include_router))
    return {"message": "Welcome to the FastAPI Postgres Integration API!"}
