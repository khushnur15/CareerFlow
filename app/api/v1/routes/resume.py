from fastapi import APIRouter, UploadFile, File
import shutil
import os
from app.utils.resume_parser import extract_text_from_pdf
from app.utils.skill_extractor import extract_skills

router = APIRouter()


@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    upload_dir = os.path.join(os.getcwd(), "uploads")

    if not os.path.isdir(upload_dir):
        os.makedirs(upload_dir)

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

    return {
    "message": "Resume uploaded successfully",
    "filename": "resume.pdf",
    "skills": skills,
    "text_preview": text[:1000]
}