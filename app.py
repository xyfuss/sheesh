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
    bilde = db.Column('bilde', db.String(100))


def __init__(self, merke, modell, vekt, bredde, pris, bilde):
    self.merke = merke
    self.modell = modell
    self.vekt = vekt
    self.bredde = bredde
    self.pris = pris
    self.bilde = bilde


@app.route('/')
def index():
    ski = db.engine.execute('SELECT * FROM ski ORDER BY bredde DESC')

    return render_template('index.html', ski=ski)


app.run(debug=True)
