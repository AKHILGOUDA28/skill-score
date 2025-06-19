from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from resume_parser import extract_text, match_skills

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload-resume/")
async def upload_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

    contents = await file.read()

    resume_text = extract_text(contents)

    score, matched, required_skills = match_skills(resume_text, job_description)

    return {
        "match_percentage": f"{score:.2f}%",
        "matched_skills": matched,
        "missing_skills": list(set(required_skills) - set(matched)),
        "detected_skills_from_jd": required_skills
    }
