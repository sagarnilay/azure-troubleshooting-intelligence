from fastapi import FastAPI
from pydantic import BaseModel

from app.database.connection import Base, engine
from app.models.case_db import Case  # noqa: F401 - registers the model with Base


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Azure Troubleshooting Intelligence",
    description="Intelligent troubleshooting platform for Windows and Azure environments",
    version="0.1.0",
)


class TroubleshootingCase(BaseModel):
    category: str
    error_code: str | None = None
    description: str


@app.get("/")
def root():
    return {
        "name": "Azure Troubleshooting Intelligence",
        "status": "running",
    }


@app.post("/cases/analyze")
def analyze_case(case: TroubleshootingCase):
    return {
        "category": case.category,
        "error_code": case.error_code,
        "description": case.description,
        "message": "Case received successfully",
    }
