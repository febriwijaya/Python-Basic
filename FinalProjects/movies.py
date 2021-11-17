"""
This is the directors module and supports all the REST actions for the
directors data
"""

from flask import make_response, abort
from config import db
from models import Directors, Movies, MoviesSchema


def read_all():
    """
    This function responds to a request for /api/directors/movies
    with the complete list of movies, sorted by movies release_date

    :return:                json list of all movies for all directors
    """
    # Query the database for all the movies
    movies = Movies.query.order_by(db.desc(Movies.release_date)).limit(5)

    # Serialize the list of movies from our data
    movies_schema = MoviesSchema(many=True)
    data = movies_schema.dump(movies)
    return data


def read_one(directors_id, movies_id):
    """
    This function responds to a request for
    /api/directors/{directors_id}/movies/{movies_id}
    with one matching movies for the associated directors

    :param directors_id:       Id of directors the movies is related to
    :param movies_id:         Id of the movies
    :return:              json string of movies contents
    """
    # Query the database for the movies
    movies = (
        Movies.query.join(Directors, Directors.directors_id == Movies.director_id)
        .filter(Directors.directors_id == directors_id)
        .filter(Movies.movies_id == movies_id)
        .one_or_none()
    )

    # Was a movies found?
    if movies is not None:
        movies_schema = MoviesSchema()
        data = movies_schema.dump(movies)
        return data

    # Otherwise, nope, didn't find that movies
    else:
        abort(404, f"Movies not found for Id: {movies_id}")


def create(directors_id, movies):
    """
    This function creates a new movies related to the passed in directors id.

    :param directors_id:       Id of the directors the movies is related to
    :param movies:     The JSON containing the movies data
    :return:               201 on success
    """
    # get the parent directors
    directors = Directors.query.filter(Directors.directors_id == directors_id).one_or_none()

    # Was a directors found?
    if directors is None:
        abort(404, f"Directors not found for Id: {directors_id}")

    # Create a movies schema instance
    schema = MoviesSchema()
    new_movies = schema.load(movies, session=db.session)

    # Add the movies to the directors and database
    directors.movies.append(new_movies)
    db.session.commit()

    # Serialize and return the newly created movies in the response
    data = schema.dump(new_movies)

    return data, 201


def update(directors_id, movies_id, movies):
    """
    This function updates an existing movies related to the passed in
    directors id.

    :param directors_id:       Id of the directors the movies is related to
    :param movies_id:         Id of the movies to update
    :param content:            The JSON containing the movies data
    :return:                200 on success
    """
    update_movies = (
        Movies.query.filter(Directors.directors_id == directors_id)
        .filter(Movies.movies_id == movies_id)
        .one_or_none()
    )

    # Did we find an existing movies?
    if update_movies is not None:

        # turn the passed in movies into a db object
        schema = MoviesSchema()
        update = schema.load(movies, session=db.session)

        # Set the id's to the movies we want to update
        update.directors_id = update_movies.director_id
        update.movies_id = update_movies.movies_id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated movies in the response
        data = schema.dump(update_movies)

        return data, 200

    # Otherwise, nope, didn't find that movies
    else:
        abort(404, f"Movies not found for Id: {movies_id}")


def delete(directors_id, movies_id):
    """
    This function deletes a movies from the movies structure

    :param id:   Id of the directors the movies is related to
    :param id:     Id of the movies to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the movies requested
    movies = (
        Movies.query.filter(Directors.directors_id == directors_id)
        .filter(Movies.movies_id == movies_id)
        .one_or_none()
    )

    # did we find a movies?
    if movies is not None:
        db.session.delete(movies)
        db.session.commit()
        return make_response(
            "Movies {movies_id} deleted".format(movies_id=movies_id), 200
        )

    # Otherwise, nope, didn't find that movies
    else:
        abort(404, f"Movies not found for Id: {movies_id}")