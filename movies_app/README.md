# YearOne Movies Backend

Please see the instructions below for proper setup of the Flask backend for the takehome application. If you would like to setup the frontend please go to [https://github.com/Johnny112F/YearOne-Takehome-Frontend].

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