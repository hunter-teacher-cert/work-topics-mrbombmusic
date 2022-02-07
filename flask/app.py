from flask import Flask
from flask import render_template, flash, redirect
import random


from imdb import IMDb
import pprint

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class EnterActor(FlaskForm):
    actorName = StringField('Actor Name', validators=[DataRequired()])
    submit = SubmitField('Get Movies')

ia = IMDb()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'



@app.route("/rand")
def randomnumber():
  i = random.randrange(100)
  color = False
  if i % 2 == 0:
    color = True
  return render_template("lucky.html", title="Random Numbers", number=i, fontColor=color)

name = ""

@app.route("/find", methods=['GET', 'POST'])
def find():
    form = EnterActor()
    if form.validate_on_submit():
        find.name = form.actorName.data #https://stackoverflow.com/questions/10139866/calling-variable-defined-inside-one-function-from-another-function
        return redirect('/film')
    return render_template("findActor.html", title="Find an Actor", form=form)

@app.route("/film")
def findMovie():
    person = ia.search_person(str(find.name))
    id = person[0].personID
    actor = ia.get_person(id, info='filmography')
    films = actor.get('filmography')
    movies = films.get("actor")
    return render_template("movies.html", title="Movies!", movies=movies, actor=person[0])



@app.route("/greetings")
def indx():
    users = [
    {'username': 'Mr Bomb',
    'greeting': 'Hello',
    'color':'red'},
    {'username': 'Steve-O',
    "greeting": 'Hola',
    'color':'blue'},
    {'username': 'Dr. Hugs Kyomius',
    'greeting': 'γεια σας',
    'color':'green'}
    ]
    return render_template("greetings.html", users=users)

@app.route("/")
def index():
  return "<h1>Hello World from my local computer!</h1>"


app.run(host="0.0.0.0",port=5000,debug=True)
