# Cinefast 🎬

A movie catalog website built with FastAPI, Jinja2, Bootstrap, and Python.

## 📖 About

Cinefast is a web development project focused on backend development using **FastAPI** to handle application routes and serve dynamic movie pages.

The application uses **Jinja2** for server-side HTML templating, **Bootstrap CSS** for responsive layouts, and **vanilla JavaScript** for basic interactivity. Movie information is currently stored in a Python list.

## ✨ Features

* Movie catalog with titles, genres, years, ratings, and descriptions
* Dynamic movie detail pages
* Individual routes for each movie
* Reusable HTML templates with Jinja2
* Navigation between pages
* Custom dark-themed interface
* Responsive layout with Bootstrap
* Static file serving for CSS, icons, and movie posters
* Automatic current year in the footer
* About page

## 🛠️ Technologies

* **Python** — application logic and movie data
* **FastAPI** — backend framework and routing
* **Uvicorn** — ASGI server for running the application
* **Jinja2** — server-side HTML templating
* **Bootstrap 5** — responsive layouts and UI components
* **CSS3** — custom styling and dark theme
* **JavaScript** — basic interactivity and dynamic content

## 📂 Project Structure

```text
Cinefast/
├── main.py
├── requirements.txt
├── .gitignore
├── static/
│   ├── css/
│   │   └── main.css
│   ├── icons/
│   │   └── favicon.ico
│   └── movie_posters/
│       └── default.png
├── templates/
│   ├── layout.html
│   ├── home.html
│   ├── movie.html
│   └── about.html
└── README.md
```

### Files

* `main.py` — FastAPI application, routes, and movie data
* `requirements.txt` — Python dependencies
* `.gitignore` — files and directories excluded from version control
* `templates/layout.html` — shared layout, navigation, and footer
* `templates/home.html` — movie catalog and movie cards
* `templates/movie.html` — individual movie details
* `templates/about.html` — project information page
* `static/css/main.css` — custom styles and visual theme
* `static/icons/favicon.ico` — website favicon
* `static/movie_posters/default.png` — default movie poster
* `README.md` — project documentation

## ▶️ How to Run

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/cinefast.git
cd cinefast
```

Replace `YOUR_USERNAME` with your GitHub username or use your repository's actual URL.

### Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

On Linux or macOS:

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Start the development server

```bash
uvicorn main:app --reload
```

Open the application in your browser:

```text
http://127.0.0.1:8000
```

## 🎬 How It Works

Cinefast uses FastAPI to define application routes and Jinja2 to render HTML pages dynamically.

The application provides three main routes:

* `/` — displays the movie catalog.
* `/filmes/{movie_id}` — displays the details of a specific movie.
* `/about` — displays information about the project.

Movie information is stored in a Python list and passed to the templates as context data. Jinja2 iterates through the movies to generate the catalog and display individual movie details.

The shared `layout.html` template provides consistent navigation, styling, and footer elements across the website.

## 🚀 Future Improvements

* Integrate a database to persist movie information
* Implement search and filtering by genre or year
* Add pagination to the movie catalog
* Improve error handling for nonexistent movie IDs
* Add administrative features to manage movies

## 👤 Author

### More about me

* GitHub: [@Vanelli-Afk](https://github.com/Vanelli-afk)
* LinkedIn: [Miguel Vanelli](https://linkedin.com/in/miguel-vanelli)

---
