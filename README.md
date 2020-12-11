# URL Shortener

-   This is a URL shortener built using the Flask microframework of python.
-   The site also shows the number of times a given shortened URL has been visited
-   To replicate this project on your machine, follow these steps:
    1. **git clone** this repo
    2. Run **pipenv install -r requirements.txt**, to install all dependencies from the pipfile.lock
    3. Create a .env file to store details of sqlite db URI as **DATABASE_URL=sqlite:///name.db**
    4. Create a .flaskenv file to set **FLASK_APP = url_shortener** and **FLASK_ENV = development**, so that you can run the app in development.
    5. **flask run** is the command to start the development server(Note: execute this inside the pipenv shell)
