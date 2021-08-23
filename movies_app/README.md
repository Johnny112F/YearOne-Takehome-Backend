# YearOne Movies Backend

Please see the instructions below for proper setup of the Flask backend for the takehome application. If you would like to setup the frontend please go to [https://github.com/Johnny112F/YearOne-Takehome-Frontend].

See the deployed app in action at [YearOneMovies](https://fretful-hands.surge.sh/)

## Backend Setup

1.Navigate to the movies_app folder in the backend. Create a virtual environment using *python3 -m venv venv*.

2.Activate your virtual environment *using source venv/bin/activate*. Anytime you are running or testing the application remember to activate your venv first.

3.Install the requirements using the command pip install - r requirements.txt.

4.You must create a database for the application called "movies". In the terminal move into PSQL by typing "psql",
then type CREATE DATABASE movies. You may have to run app.py in ipython from the movies_app folder in order for the tables to created in the database correctly.

5.Sign up for a free account at [https://developers.themoviedb.org/3/getting-started/introduction]. You will need an API key to use this application.

6. Create a file called .env in the movies_app folder and place the variables API_BASE_URL = https://api.themoviedb.org/3 and API_KEY = [Your api key in strings placed here from tmbd]. Make sure your .env file is not exposed if you are pushing the repo to github.

7.Use the command "flask run" while in teh movies_app folder from the terminal to start the server.

8. You can test the backend routes in insomnia by importing the request collection from this backend or by creating your own.

HomePage

<img width="400" alt="Screen Shot 2021-08-22 at 3 04 12 PM" src="https://user-images.githubusercontent.com/50811190/130369464-ca9ae45f-c6db-40f7-acea-8121d99ff83c.png">

SearchResults

<img width="400" alt="Screen Shot 2021-08-22 at 3 05 52 PM" src="https://user-images.githubusercontent.com/50811190/130369533-1e6f9746-718f-4489-873b-8874e9f21217.png">

MovieDetails

<img width="400" alt="Screen Shot 2021-08-22 at 4 46 36 PM" src="https://user-images.githubusercontent.com/50811190/130369603-4f25afa6-f533-4e23-a086-b2b43247e405.png">

Review

<img width="400" alt="Screen Shot 2021-08-22 at 4 46 52 PM" src="https://user-images.githubusercontent.com/50811190/130369625-2ba62d88-8aa1-4246-b024-c1e334c79c9f.png">

