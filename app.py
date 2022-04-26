from flask import Flask, request, jsonify
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('movie', user='emmanuel',
                        password='1234', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Movie(BaseModel):
    position = IntegerField()
    const = CharField()
    created = CharField()
    modified = CharField()
    description = CharField()
    title = CharField()
    url = CharField()
    title_type = CharField()
    imdb_rating = IntegerField()
    runtime_mins = IntegerField()
    year = IntegerField()
    genres = CharField()
    num_votes = IntegerField()
    release_date = CharField()
    directors = CharField()


db.connect()
db.drop_tables([Movie])
db.create_tables([Movie])


Movie(position="1", const="tt0468569", created="2012-08-13", modified="2012-08-13", description="", title="The Dark Knight", url="https://www.imdb.com/title/tt0468569/", title_type="movie",
      imdb_rating=9.1, runtime_mins=152, year=2008, genres="Action, Crime, Drama, Thriller", num_votes=2530527, release_date="2008-07-14", directors="Christopher Nolan").save()

Movie(position="2", const="tt4154796", created="2019-05-07", modified="2019-05-07", description="", title="Avengers: Endgame", url="https://www.imdb.com/title/tt4154796/", title_type="movie",
      imdb_rating=8.4, runtime_mins=181, year=2019, genres="Action, Adventure, Drama, Sci-Fi", num_votes=1031811, release_date="2019-04-22", directors="Anthony Russo, Joe Russo").save()

Movie(position="3", const="tt4154756", created="2018-08-06", modified="2018-08-06", description="", title="Avengers: Infinity War", url="https://www.imdb.com/title/tt4154756/", title_type="movie",
      imdb_rating=8.5, runtime_mins=149, year=2018, genres="Action, Adventure, Sci-Fi", num_votes=997179, release_date="2018-04-23", directors="Anthony Russo, Joe Russo").save()


Movie(position="4", const="tt3315342", created="2017-03-06", modified="2017-03-06", description="", title="Logan", url="https://www.imdb.com/title/tt3315342/", title_type="movie",
      imdb_rating=8.1, runtime_mins=137, year=2017, genres="Action, Drama, Sci-Fi, Thriller", num_votes=721122, release_date="2017-02-17", directors="James Mangold").save()

Movie(position="5", const="tt1345836", created="2012-08-13", modified="2012-08-13", description="", title="The Dark Knight Rises", url="https://www.imdb.com/title/tt1345836/",
      title_type="movie", imdb_rating=8.4, runtime_mins=164, year=2012, genres="Action, Crime, Drama", num_votes=1638475, release_date="2012-07-16", directors="Christopher Nolan").save()

app = Flask(__name__)


@app.route('/movie/', methods=['GET', 'POST'])
@app.route('/movie/<id>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(id=None):
    if request.method == 'GET':
        if id:
            return jsonify(model_to_dict(Movie.get(Movie.id == id)))
        else:
            movielist = []
            for movie in Movie.select():
                movielist.append(model_to_dict(movie))
            return jsonify(movielist)

    if request.method == 'PUT':
        return 'PUT request'

    if request.method == 'POST':
        new_movie = dict_to_model(Movie, request.get_json())
        new_movie.save()
        return jsonify({"success": True})

    if request.method == 'DELETE':
        return 'DELETE request'


app.run(debug=True)
