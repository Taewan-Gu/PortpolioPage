import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import database, models
from routers.activity import router as activity_router
from routers.goal import router as goal_router
from routers.resume import router as resume_router
from routers.user import router as user_router

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api")
async def read_root():
    return {"Health Check": True}


app.include_router(user_router, prefix="/api")
app.include_router(goal_router, prefix="/api/goals")
app.include_router(activity_router, prefix="/api/activities")
app.include_router(resume_router, prefix="/api/resume")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3006)
