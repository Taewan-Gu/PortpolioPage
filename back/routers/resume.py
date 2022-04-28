from os import path
from sys import path as pth

from fastapi import APIRouter
from fastapi.responses import FileResponse

pth.append(path.dirname(path.abspath(path.dirname(__file__))))
parent_route = path.dirname(path.abspath(path.dirname(__file__)))

router = APIRouter(tags=["resume"])


@router.get("/download", description="resume 다운로드")
def get_resume():
    try:
        open(f"{parent_route}/assets/sample.png")
        response = FileResponse(f"{parent_route}/assets/sample.png")
        response["Content-Disposition"] = 'attachment; filename="sample.png"'
        return
    except Exception:
        return FileResponse(f"{parent_route}/assets/activities/default.png")
