from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.orchestrator import generate_essay_pipeline

router = APIRouter()

class StudentProfile(BaseModel):
    interests: str
    achievements: str
    challenges: str
    goals: str

class EssayRequest(BaseModel):
    student_profile: StudentProfile
    tone: str

@router.post("/generate-essay")
def generate_essay(req: EssayRequest):
    result = generate_essay_pipeline(req.student_profile.dict(), req.tone)
    return result