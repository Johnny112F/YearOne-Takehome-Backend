from flask import Flask, request
import requests
from models import db, connect_db, Movie
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
    r"/": {
        "origins": "*"
    }
})

app.config['CORS_HEADERS'] = 'Content-Type'
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///movies"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = False

connect_db(app)

API_BASE_URL = "https://api.themoviedb.org/3"

API_KEY = "025df31fafd1a25ca2c09af81ad939a7"


@app.route("/movies/search", methods=["GET"])
@cross_origin()
def search_movies():
    """Search API for movies"""

    term = request.args["term"]
    page = request.args.get("page", 1)

    querystring = {"api_key": API_KEY, "query": term, "page": page}

    res = requests.get(f"{API_BASE_URL}/search/movie", params=querystring)
    data = res.json()
    
    return(data, 200)


@app.route("/movies/<movie_id>", methods=["GET"])
@cross_origin()
def movie_detail(movie_id):
    """get details of a specific movie"""
    
    movie = Movie.query.get(movie_id)
    
    querystring = {"api_key": API_KEY}
    
    details_resp = requests.get(f"{API_BASE_URL}/movie/{movie_id}", params=querystring)
    details = details_resp.json()
    
    title = details["title"]
    release_year = details["release_date"][:4]
    description = details["overview"]

    credits_resp = requests.get(f"{API_BASE_URL}/movie/{movie_id}/credits", params=querystring)
    crew = credits_resp.json()['crew']
    director = [x for x in crew if x['job'] == "Director"][0]["name"]

    movie_details = {
                     "title": title, 
                     "release_year": release_year, 
                     "description": description, 
                     "director": director,
                     "thumbs_up": movie.thumbs_up or 0,
                     "thumbs_down": movie.thumbs_down or 0
                    }
    
    return (movie_details, 200)


@app.route("/movies/<movie_id>/rate", methods=["POST"])
@cross_origin()
def rate_movie(movie_id):
    """Check database for movie rating and increment thumbs up vote"""
    # filter to see if the movie already exists in db
    movie = Movie.query.get(movie_id)
    rating = request.json.get("rating")
    title = request.json.get("title")
    
    if movie:
        movie.handle_rating(rating)
    else:
        movie = Movie(title=title, movie_id=movie_id)
        movie.handle_rating(rating)
        db.session.add(movie)

    db.session.commit()
    breakpoint()
    return(title)