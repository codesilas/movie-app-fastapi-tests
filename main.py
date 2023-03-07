from fastapi import FastAPI, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
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
            "category": "category"
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
    return JSONResponse(content=movies)

@app.get("/movies/{id}", tags=["movies"])
def get_movie(id: int = Path()):
    for item in movies:
        if item["id"] == id:
            return JSONResponse(content=item)
        return JSONResponse(content=[])

@app.get("/movies/", tags=["movies"])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)):
    # usando list comprehension
    data = [movie for movie in movies if movie['category'] == category]
    return JSONResponse(content=data)

@app.post("/movies/", tags=["movies"])
def create_movies(movie: Movie):
    movies.append(movie)
    return JSONResponse(content={"message": "Se registró la pelicula"})

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
            return JSONResponse(content={"message": "Se modificó la pelicula"})

@app.delete("/movies{id}", tags=["movies"])
def delete_movie(id:int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return JSONResponse(content={"message":"Se eliminó la pelicula"})