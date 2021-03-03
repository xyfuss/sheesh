from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///musikkalbum.sqlite3'

db = SQLAlchemy(app)


class musikkalbum(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    artist = db.Column('artist', db.String(100))
    release_date = db.Column('release_date', db.Integer)
    genre = db.Column('genre', db.String(100))
    best_song = db.Column('best_song', db.String(100))
    overall_rating = db.Column('overall_rating', db.Integer)
    cover = db.Column('cover', db.String(200))


def __init__(self, name, artist, release_date, genre, best_song, overall_rating, cover, songname, albumid, rating, track_number):
    self.name = name
    self.artist = artist
    self.release_date = release_date
    self.genre = genre
    self.best_song = best_song
    self.overall_rating = overall_rating
    self.cover = cover
    self.songname = name
    self.albumid = albumid
    self.rating = rating
    self.track_number = track_number


class sanger(db.Model):
    songid = db.Column('id', db.Integer, primary_key=True)
    albumid = db.Column('albumid', db.Integer, db.ForeignKey('album.id'))
    songname = db.Column('name', db.String(100))
    rating = db.Column('rating', db.Integer)
    track_number = db.Column('track_number', db.Integer)


@ app.route('/')
def index():
    musikkalbum = db.engine.execute('SELECT * FROM album')

    return render_template('index.html', musikkalbum=musikkalbum)


@ app.route('/<id>')
def album(id):
    musikkalbum = db.engine.execute(
        f'SELECT * FROM album WHERE id = "{id}" ')
    sanger = db.engine.execute(
        f'SELECT * FROM sanger WHERE albumid = "{id}"')
    return render_template('albumpage.html', musikkalbum=musikkalbum, sanger=sanger)


app.run(debug=True)
