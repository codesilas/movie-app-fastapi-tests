from fastapi import FastAPI, Body, Path
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version ="0.0.1"

class Movie(BaseModel):
    # id se puede validar como:
    # id: int | None = None
    
    #así se hace con typing y Optional
    id: Optional[int] = None
    title: str = Field(max_length=15, min_length=5)
    overview: str = Field(max_length=50, min_length=15)
    year: int = Field(le=2030)
    rating: float = Field(lt=1.1) 
    category: str = Field(min_length=2,max_length=10)
    
    # lo siguiente se toman como valores por default
    class config:
        example_schema ={
            "id": 1,
            "title": "Movie name",
            "overview": "Movie summary",
            "year": 2010,
            "rating": 0.0,
            "category": "Genre"
        }


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
def create_movies(movie: Movie):
    movies.append(movie)
    return movies

@app.put("/movies{id}", tags=["movies"] )
def update_movie(id:int, movie:Movie):
    for item in movies:
        if item["id"] == id:
            item["title"] = movie.title
            item["overview"] = movie.overview
            item["year"] = movie.year
            item["year"] = movie.year
            item["rating"] = movie.rating
            item["category"] = movie.category

@app.delete("/movies{id}", tags=["movies"])
def delete_movie(id:int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return movies