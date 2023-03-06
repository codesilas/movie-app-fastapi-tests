from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version ="0.0.1"

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'
    }
]


@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('<h1 style=color:red> Hola Mundo </h1>')


@app.get('/movies', tags=['movies'])
def get_movies():
    return movies

@app.get("/movies/{id}", tags=["movies"])
def get_movie(id: int):
    return id

@app.get("/movies/", tags=["movies"])
def get_movies_by_category(category: str):
    
    # usando list comprehension
    return [movie for movie in movies if movie['genre'] == category]

@app.post("/movies/", tags=["movies"])
def create_movies(id:int = Body(), title:str = Body(), overview:str = Body(), year:int = Body(), rating:float = Body(), category:str = Body()):
    movies.append({
        'id': id,
        'title': title,
        'overview': overview,
        'year': year,
        'rating': rating,
        'category': category
    })
    return movies

@app.put("/movies{id}", tags=["movies"] )
def update_movie(id:int, title:str = Body(), overview:str = Body(), year:int = Body(), rating:float = Body(), category:str = Body()):
    # logica para editar la pelicula
    