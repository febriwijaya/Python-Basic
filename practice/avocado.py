"""
This is the people module and supports all the REST actions for the
people data
"""

from flask import make_response, abort
from config import db
from models import Avocado, AvocadoSchema


def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        json string of list of people
    """
    # Create the list of people from our data
    avocado_item = Avocado.query.order_by(Avocado.regionid).all()

    # Serialize the data for the response
    avocado_schema = AvocadoSchema(many=True)
    data = avocado_schema.dump(avocado_item)
    return data


def read_one(regionid):
    """
    This function responds to a request for /api/people/{person_id}
    with one matching person from people

    :param person_id:   Id of person to find
    :return:            person matching id
    """
    # Get the person requested
    avocado_item = Avocado.query.filter(Avocado.regionid == regionid).one_or_none()

    # Did we find a person?
    if avocado_item is not None:

        # Serialize the data for the response
        avocado_schema = AvocadoSchema()
        data = avocado_schema.dump(avocado_item)
        return data

    # Otherwise, nope, didn't find that person
    else:
        abort(
            404,
            f"Avocado not found for Region Id: {regionid}",
        )


def create(avocado):
    """
    This function creates a new person in the people structure
    based on the passed in person data

    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    regionid = avocado.get("regionid")

    existing_region = (
        Avocado.query.filter(Avocado.regionid == regionid)
        .one_or_none()
    )

    # Can we insert this person?
    if existing_region is None:

        # Create a person instance using the schema and the passed in person
        schema = AvocadoSchema()
        new_avocado = schema.load(avocado, session=db.session)

        # Add the person to the database
        db.session.add(new_avocado)
        db.session.commit()

        # Serialize and return the newly created person in the response
        data = schema.dump(new_avocado)

        return data, 201

    # Otherwise, nope, person exists already
    else:
        abort(
            409,
            f"Region : {regionid} already exists!",
        )


def update(regionid, avocado):
    """
    This function updates an existing person in the people structure

    :param person_id:   Id of the person to update in the people structure
    :param person:      person to update
    :return:            updated person structure
    """
    # Get the person requested from the db into session
    update_person = Avocado.query.filter(
        Avocado.regionid == regionid
    ).one_or_none()

    # Did we find an existing person?
    if update_person is not None:

        # turn the passed in person into a db object
        schema = AvocadoSchema()
        update = schema.load(avocado, session=db.session)

        # Set the id to the person we want to update
        update.regionid = update_person.regionid

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated person in the response
        data = schema.dump(update_person)

        return data, 200

    # Otherwise, nope, didn't find that person
    else:
        abort(404, f"Region Id: {regionid} Not Found")


def delete(regionid):
    """
    This function deletes a person from the people structure

    :param person_id:   Id of the person to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the person requested
    avocado = Avocado.query.filter(Avocado.regionid == regionid).one_or_none()

    # Did we find a person?
    if avocado is not None:
        db.session.delete(avocado)
        db.session.commit()
        return make_response(
            f"Avocado with region id {regionid} has been deleted", 200
        )

    # Otherwise, nope, didn't find that person
    else:
        abort(
            404,
            f"Region id : {regionid} not found",
        )