from flask import Flask
from flask import render_template, flash, redirect, request, session
import random

#imports Cinemagoer library to access info from IMDb
from imdb import Cinemagoer
from imdb.Person import Person
import pprint

#Form libray imports taken from Flask Mega tutorial
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class EnterActor(FlaskForm):
    actorName = StringField('Actor Name', validators=[DataRequired()])
    submit = SubmitField('Get Movies')

ia = Cinemagoer()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

#This page will choose a random actor and a random movie or TV show frmo their IMDb filmography
@app.route("/rand")
def randomnumber():
  number="%07d" % random.randint(0,999999)
  actor = ia.get_person(number, info='filmography')
  films = actor.get('filmography')
  movies = []
  if "actress" in films:
      movies = films.get("actress")
  elif "actor" in films:
      movies = films.get("actor")
  if len(movies) > 0:
      num_of_movies = len(movies)
      i = random.randint(0, num_of_movies -1)
      randomMovie = movies[i]
  else:
      randomMovie = actor['name'] + "does not have any listed acting credits"
  return render_template("lucky.html", title="Random Actor", number=actor, movie=randomMovie)#, fontColor=color)

#This function finds the filmography of a specific actor
name = ""
actor = ""
def find_actor_movies(actorName):
    person = ia.search_person(actorName)
    id = person[0].personID
    find.actor = ia.get_person(id, info='filmography')
    films = find.actor.get('filmography')
    movies = []
    if "actress" in films:
        movies = films.get("actress")
    elif "actor" in films:
        movies = films.get("actor")
    return movies

#This page allows the user to search the filmography of a specific actor
searched_actors = [""];
@app.route("/find", methods=['GET', 'POST'])
def find():
    form = EnterActor()
    #This session is meant to keep track of how many different actors have been searched while visiting the site.
    print(session)
    if 'count' not in session:
        session['count'] = searched_actors
    else:
        session['count'] = session['count'] + 1
    if form.validate_on_submit():
        find.name = form.actorName.data #https://stackoverflow.com/questions/10139866/calling-variable-defined-inside-one-function-from-another-function
        #This is meant to keep track of all the different actors which have been searched during site visit
        if searched_actors[0] == "":
            searched_actors.append(find.name)
            searched_actors.pop(0)
        else:
            searched_actors.insert(0,find.name)
        #Page will redirect to different page to display actor's filmography
        return redirect('/film')
    return render_template("findActor.html", title="Find an Actor", form=form, actorList=searched_actors, count=session['count'])

#This page will display the filmography of the actor searched from the previosu page
@app.route("/film")
def findMovie():
    movies = find_actor_movies(str(find.name))
    if len(movies) == 0:
        movies.append(str(find.name) + " does not have any listed acting credits")
    return render_template("movies.html", title="Movies!", movies=movies, actor=find.actor)

#This function cross references the filmographies of two actors to see if they share any acting credits
def find_movie_match(actor1, actor2):
    actor1_movies = find_actor_movies(actor1)
    actor2_movies = find_actor_movies(actor2)
    # https://www.kite.com/python/answers/how-to-find-the-intersection-of-two-lists-in-python
    same_movie = set.intersection(set(actor1_movies), set(actor2_movies))
    if len(list(same_movie)) != 0:
        return list(same_movie)
    else:
        return False

#This page allows user to search two different actors to see if they share any acting credits
@app.route("/match", methods=['GET', 'POST'])
def matchActors():
    if request.method=='GET':
        return render_template("match.html")
    else:
        actor1 = request.form["actor1"]
        actor2 = request.form["actor2"]
        if actor1 == "" or actor2 == "":
            error = "You forgot to enter two actor names!"
        else:
            movie_match = find_movie_match(str(actor1), str(actor2))
            error = ""
        return render_template("match.html", actor1=actor1, actor2=actor2, result=movie_match, error=error)

#This page is a greeting welcoming user to the page in 3 languages (English, Spanish and Greek)
@app.route("/greetings")
def greeting():
    users = [
    {'username': 'Movie Fan',
    'greeting': 'Hello',
    'color':'red'},
    {'username': 'Fanático del cine',
    "greeting": 'Hola',
    'color':'blue'},
    {'username': 'θαυμαστής του κινηματογράφου',
    'greeting': 'γεια σας',
    'color':'green'}
    ]
    return render_template("greetings.html", users=users)

#This page redirects to greeting page if no route name is provided
@app.route("/")
def index():
  return redirect("/greetings")


app.run(host="0.0.0.0",port=5000,debug=True)
