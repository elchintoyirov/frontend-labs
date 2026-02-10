from fastapi import Request, APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

posts = [
    {
        "title": "First post",
        "slug": "first-post",
        "date": "January 20, 2026",
        "excerpt": "First post as preview",
    },
    {
        "title": "Second post",
        "slug": "second-post",
        "date": "January 20, 2026",
        "excerpt": "Second post as preview",
    },
    {
        "title": "Third post",
        "slug": "third-post",
        "date": "January 20, 2026",
        "excerpt": "Third post as preview",
    },
]

@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "posts": posts},
    )


@router.get("/post/{slug}")
async def post_detail(request: Request, slug: str):
    post = next((p for p in posts if p["slug"] == slug), None)

    if not post:
        return templates.TemplateResponse(
            "404.html",
            {"request": request},
            status_code=404,
        )

    return templates.TemplateResponse(
        "post.html",
        {"request": request, "post": post},
    )
