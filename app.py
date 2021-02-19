from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///musikkalbum.sqlite3'

db = SQLAlchemy(app)


class ski(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    merke = db.Column('merke', db.String(100))
    modell = db.Column('modell', db.String(100))
    vekt = db.Column('vekt', db.Integer)
    bredde = db.Column('bredde', db.Integer)
    pris = db.Column('pris', db.Integer)
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
