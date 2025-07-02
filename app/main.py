from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn

from app.routes import employee as employee_router
from app.bin.create_table import create_tables
from app.bin.seed_data import seed_data
from app.utils.rate_limiter import RateLimitMiddleware

# Lifespan context to replace on_event("startup")
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("App startup: Creating tables and seeding data...")
    create_tables()
    seed_data()
    yield
    print("App shutdown (if needed cleanup)")

app = FastAPI(
    title="Basic FastAPI App",
    description="A simple FastAPI application to demonstrate Employee Search filter functionality.",
    lifespan=lifespan
)

# Middlewares
app.add_middleware(RateLimitMiddleware)

# Register routes
app.include_router(employee_router.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Welcome to Employee Microservice"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
