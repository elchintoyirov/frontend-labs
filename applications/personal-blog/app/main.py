from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from app.routes import router as blog_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

app.include_router(blog_router)

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})