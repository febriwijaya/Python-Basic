"""
Main module of the server file
"""

# 3rd party moudles
from flask import render_template

# Local modules
import config


# Get the application instance
connex_app = config.connex_app

# Read the swagger.yml file to configure the endpoints
connex_app.add_api("swagger.yml")


# Create a URL route in our application for "/"
@connex_app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/

    :return:        the rendered template "home.html"
    """
    return render_template("home.html")


# Create a URL route in our application for "/directors"
@connex_app.route("/directors")
@connex_app.route("/directors/<int:directors_id>")
def directors(directors_id=""):
    """
    This function just responds to the browser URL
    localhost:5000/directors

    :return:        the rendered template "directors.html"
    """
    return render_template("directors.html", directors_id=directors_id)


# Create a URL route to the movies page
@connex_app.route("/directors/<int:directors_id>")
@connex_app.route("/directors/<int:directors_id>/movies")
@connex_app.route("/directors/<int:directors_id>/movies/<int:movies_id>")
def movies(directors_id, movies_id=""):
    """
    This function responds to the browser URL
    localhost:5000/movies/<directors_id>

    :param directors_id:   Id of the directors to show movies for
    :return:            the rendered template "movies.html"
    """
    return render_template("movies.html", directors_id=directors_id, movies_id=movies_id)


if __name__ == "__main__":
    connex_app.run(debug=True)