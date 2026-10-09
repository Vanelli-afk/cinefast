from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
    )

templates = Jinja2Templates(directory="templates")

movies: list[dict] = [
    {
        "id": 1,
        "title": "Project Hail Mary",
        "genre": "Hard Sci-Fi",
        "year": 2026,
        "rating": 8.2,
        "description": "A science teacher wakes up alone on a spaceship. As his memory returns, he uncovers a mission to stop a mysterious substance killing Earth's sun, and realizes that an unexpected friendship may be the key."
    },
    {
        "id": 2,
        "title": "Ponyo",
        "genre": "Animation",
        "year": 2026,
        "rating": 7.6,
        "description": "A five-year-old boy develops a relationship with Ponyo, a young goldfish princess who longs to become a human after falling in love with him."
    },
    {
        "id": 3,
        "title": "Spider-Man: Brand New Day",
        "genre": "Superhero",
        "year": 2026,
        "rating": 8.0,
        "description": "A forgotten Peter Parker lives alone as a full-time Spider-Man until mounting pressure triggers a dangerous change and a powerful new enemy emerges."
    },
]

@app.get("/", include_in_schema=False, name="home")
def home(request: Request):
    return templates.TemplateResponse(
        request, 
        "home.html", 
        {"title": "Home", "movies": movies},
    )

@app.get("/filmes/{movie_id}", name="movie")
def movie(request: Request, movie_id: int):
    for movie in movies:
        if movie_id == movie["id"]:
            movie_data = movie

    return templates.TemplateResponse(
        request,
        "movie.html",
        {
            "title": movie_data["title"],
            "movie": movie_data
        }
    )

@app.get("/about", include_in_schema=False, name="about")
def about(request: Request):
    return templates.TemplateResponse(
        request,
        "about.html",
        {
            "title": "About",
        }
    )