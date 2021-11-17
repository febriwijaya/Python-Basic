from datetime import datetime
from config import db, ma
from marshmallow import fields

class Directors(db.Model):
    __tablename__ = 'directors'
    directors_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    gender = db.Column(db.Integer)
    uid = db.Column(db.Integer)
    department = db.Column(db.String)
    movies = db.relationship(
        'Movies',
        backref='directors',
        cascade='all, delete, delete-orphan',
        single_parent=True,
        order_by='desc(Movies.release_date)'
    )

class Movies(db.Model):
    __tablename__ = 'movies'
    movies_id = db.Column(db.Integer, primary_key=True)
    original_title = db.Column(db.String)
    budget = db.Column(db.Integer)
    popularity = db.Column(db.Integer)
    release_date = db.Column(db.String)
    revenue = db.Column(db.Integer)
    title = db.Column(db.String)
    vote_average = db.Column(db.String)
    vote_count = db.Column(db.Integer)
    overview = db.Column(db.String)
    tagline = db.Column(db.String)
    uid = db.Column(db.Integer)
    director_id = db.Column(db.Integer, db.ForeignKey('directors.directors_id'))

class DirectorsSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Directors
        # sqla_session = db.session
        load_instance = True

    movies = fields.Nested('DirectorsMoviesSchema', default=[], many=True)

class DirectorsMoviesSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    movies_id = fields.Int()
    original_title = fields.Str()
    budget = fields.Int()
    popularity = fields.Int()
    release_date = fields.Str()
    revenue = fields.Int()
    title = fields.Str()
    vote_average = fields.Str()
    vote_count = fields.Int()
    overview = fields.Str()
    tagline = fields.Str()
    uid = fields.Int()
    director_id = fields.Int()


class MoviesSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Movies
        # sqla_session = db.session
        load_instance = True

    directors = fields.Nested("MoviesDirectorsSchema", default=None)


class MoviesDirectorsSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    name = fields.Str()
    directors_id = fields.Int()
    gender = fields.Int()
    uid = fields.Int()
    department = fields.Str()