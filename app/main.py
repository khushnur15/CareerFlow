from fastapi import FastAPI
from app.api.v1.routes.auth import router as auth_router
from fastapi import FastAPI
from app.database import engine, Base
from app.models.user import User
app = FastAPI(
    title="CareerFlow AI API",
    description="AI-powered career assistant backend",
    version="1.0.0"
)
Base.metadata.create_all(bind=engine)
Base.metadata.create_all(bind=engine)
app.include_router(
    auth_router,
    prefix="/api/v1/auth",
    tags=["Authentication"]
)
@app.get("/")
def root():
    return {
        "message": "CareerFlow AI Backend Running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "CareerFlow AI Backend"
    }