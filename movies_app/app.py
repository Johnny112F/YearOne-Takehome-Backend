from flask import Flask, request
import requests
from models import db, connect_db, Movie
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['TESTING'] = False

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///movies"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = False

connect_db(app)

API_BASE_URL = os.environ.get("API_BASE_URL")
API_KEY = os.environ.get("API_KEY")


@app.route("/movies/search", methods=["GET"])
def search_movies():
    """Search API for movies"""

    term = request.args["term"]
    page = request.args.get("page", 1)

    querystring = {"api_key": API_KEY, "query": term, "page": page}

    url = f"{API_BASE_URL}/search/movie";

    res = requests.get(url, params=querystring)
    data = res.json()
    
    return(data, 200)


@app.route("/movies/<movie_id>", methods=["GET"])
def movie_detail(movie_id):
    """get details of a specific movie"""
    
    stored_details = Movie.query.get(movie_id)
    
    querystring = {"api_key": API_KEY}
    
    details_resp = requests.get(f"{API_BASE_URL}/movie/{movie_id}", params=querystring)
    details = details_resp.json()
    
    title = details["title"]
    release_year = details["release_date"][:4]
    description = details["overview"]
    poster_path = details["poster_path"]

    credits_resp = requests.get(f"{API_BASE_URL}/movie/{movie_id}/credits", params=querystring)
    crew = credits_resp.json()['crew']
    
    try:
        director = [x for x in crew if x['job'] == "Director"][0]["name"]
    except IndexError:
        director = "no director found"

    movie_details = {
                     "title": title, 
                     "release_year": release_year, 
                     "description": description, 
                     "director": director,
                     "thumbs_up": 0,
                     "thumbs_down": 0,
                     "poster_path": poster_path
                    }

    if stored_details:
        movie_details["thumbs_up"] = stored_details.thumbs_up
        movie_details["thumbs_down"] = stored_details.thumbs_down

    return (movie_details, 200)



@app.route("/movies/<movie_id>/rate", methods=["POST"])
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

    return ({"thumbs_up": movie.thumbs_up, "thumbs_down": movie.thumbs_down}, 201)