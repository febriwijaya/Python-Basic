"""
This is the directors module and supports all the REST actions for the
directors data
"""
from os import name
from flask import make_response, abort
from config import db
from models import Directors, DirectorsSchema, Movies


def read_all():
    """
    This function responds to a request for /api/directors
    with the complete lists of directors

    :return:        json string of list of directors
    """
    # Create the list of directors from our data
    directors = Directors.query.order_by(Directors.name).limit(10)

    # Serialize the data for the response
    directors_schema = DirectorsSchema(many=True)
    data = directors_schema.dump(directors)
    return data

def get_department(department):
    """
    sorting by department function from directors, this function is to search anyone who is there
    on the department of the input parameters, receive the department parameters, return list/json from directors
    that fits the criteria
    """
    directors = (Directors.query.filter(
        Directors.department.like(department)).limit(10))

    if directors is not None:
        directors_schema = DirectorsSchema(many=True)
        data = directors_schema.dump(directors)
        return data

    else:
        abort(404, f"director not found for department: {department}")

def get_name(name):
    """
    search directors by name function, accepts the name parameter to search for the name of the appropriate directors
    with input, return json/list of directors and movies that match the criteria
    """
    search = "%{}%".format(name)
    directors = (Directors.query.filter(
        Directors.name.like(search)).limit(10))

    if directors is not None:
        directors_schema = DirectorsSchema(many=True)
        data = directors_schema.dump(directors)
        return data

    else:
        abort(404, f"director not found for name: {name}")


def read_one(directors_id):
    """
    This function responds to a request for /api/directors/{directors_id}
    with one matching directors from directors

    :param directors_id:   Id of directors to find
    :return:            directors matching id
    """
    # Build the initial query
    directors = (
        Directors.query.filter(Directors.directors_id == directors_id)
        .outerjoin(Movies)
        .one_or_none()
    )

    # Did we find a directors?
    if directors is not None:

        # Serialize the data for the response
        directors_schema = DirectorsSchema()
        data = directors_schema.dump(directors)
        return data

    # Otherwise, nope, didn't find that directors
    else:
        abort(404, f"Directors not found for Id: {directors_id}")


def create(directors):
    """
    This function creates a new directors in the directors structure
    based on the passed in directors data

    :param directors:  directors to create in directors structure
    :return:        201 on success, 406 on directors exists
    """
    name = directors.get("name")
    gender = directors.get("gender")
    uid = directors.get("uid")
    department = directors.get("department")

    existing_directors = (
        Directors.query.filter(Directors.name == name)
        .filter(Directors.gender == gender)
        .filter(Directors.uid == uid)
        .filter(Directors.department == department)
        .one_or_none()
    )

    # Can we insert this directors?
    if existing_directors is None:

        # Create a directors instance using the schema and the passed in directors
        schema = DirectorsSchema()
        new_directors = schema.load(directors, session=db.session)

        # Add the directors to the database
        db.session.add(new_directors)
        db.session.commit()

        # Serialize and return the newly created directors in the response
        data = schema.dump(new_directors)

        return data, 201

    # Otherwise, nope, directors exists already
    else:
        abort(409, f"Directors {name} {gender} {uid} {department} exists already")


def update(directors_id, directors):
    """
    This function updates an existing directors in the directors structure

    :param directors_id:   Id of the directors to update in the directors structure
    :param directors:      directors to update
    :return:            updated directors structure
    """
    # Get the directors requested from the db into session
    update_directors = Directors.query.filter(
        Directors.directors_id == directors_id
    ).one_or_none()

    # Did we find an existing directors?
    if update_directors is not None:

        # turn the passed in directors into a db object
        schema = DirectorsSchema()
        update = schema.load(directors, session=db.session)

        # Set the id to the directors we want to update
        update.directors_id = update_directors.directors_id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated directors in the response
        data = schema.dump(update_directors)

        return data, 200

    # Otherwise, nope, didn't find that directors
    else:
        abort(404, f"Directors not found for Id: {directors_id}")


def delete(directors_id):
    """
    This function deletes a directors from the directors structure

    :param directors_id:   Id of the directors to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the directors requested
    directors = Directors.query.filter(Directors.directors_id == directors_id).one_or_none()

    # Did we find a directors?
    if directors is not None:
        db.session.delete(directors)
        db.session.commit()
        return make_response(f"Directors {directors_id} deleted", 200)

    # Otherwise, nope, didn't find that directors
    else:
        abort(404, f"Directors not found for Id: {directors_id}")