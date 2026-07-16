from fastapi import APIRouter, UploadFile, File
import shutil
import os

from app.utils.resume_parser import extract_text_from_pdf
from app.utils.skill_extractor import extract_skills
from app.utils.job_matcher import match_jobs
from app.utils.roadmap_generator import generate_roadmap

router = APIRouter()


@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    upload_dir = os.path.join(os.getcwd(), "uploads")

    if not os.path.exists(upload_dir):
        os.mkdir(upload_dir)

    file_path = os.path.join(
        upload_dir,
        "resume.pdf"
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    text = extract_text_from_pdf(file_path)

    skills = extract_skills(text)

    job_matches = match_jobs(skills)

    roadmap = generate_roadmap(job_matches)

    return {
        "message": "Resume uploaded successfully",
        "filename": "resume.pdf",
        "skills": skills,
        "recommended_roles": job_matches,
        "learning_roadmap": roadmap,
        "text_preview": text[:500]
    }