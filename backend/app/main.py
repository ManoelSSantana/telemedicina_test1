from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import auth, patients, professionals

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth.router)
app.include_router(patients.router)
app.include_router(professionals.router)

@app.get("/")
async def root():
    return {"message": "Sistema de Telemedicina API"}

@app.get("/api/health")
async def health_check():
    return {"status": "online"}
    return {"status": "online"}
