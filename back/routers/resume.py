from os import path
from sys import path as pth

from fastapi import APIRouter
from fastapi.responses import FileResponse


router = APIRouter(tags=["resume"])
parent_route = path.dirname(path.abspath(path.dirname(__file__)))


@router.get("/download", description="resume download")
def get_resume():
    return FileResponse(f"{parent_route}/assets/resume.pdf", filename="resume.pdf")

@router.get("/html", description="resume html")
def get_resume():
    return FileResponse(f"{parent_route}/assets/resume.html")
