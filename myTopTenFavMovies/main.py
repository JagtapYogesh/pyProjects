from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
db = SQLAlchemy()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
Bootstrap(app)
db.init_app(app)

class Movie(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.String, nullable=True)
    release_date = db.Column(db.String, nullable=True)
    rating = db.Column(db.String, nullable=True)
    review = db.Column(db.String, nullable=True)
    overview = db.Column(db.String, nullable=True)

with app.app_context():
    db.create_all()


class Edit_movie(FlaskForm):
    rating = StringField(label="Your rating out of 10 eg. 5.7", validators=[DataRequired()])
    review = StringField(label="Your review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


class Add_movie(FlaskForm):
    movie_name = StringField(label="Movie name", validators=[DataRequired()])
    release_date = StringField(label="Release Date", validators=[DataRequired()])
    rating = StringField(label="Rate the movie", validators=[DataRequired()])
    review = StringField(label="Review about movie", validators=[DataRequired()])
    overview = StringField(label="Overview about movie", validators=[DataRequired()])
    submit = SubmitField(label="Add")


@app.route("/")
def home():
    movies_list_db = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars()
    movies_list = []
    id = 1
    for item in movies_list_db:
        movie = {
            "rank": id,
            "name": item.movie_name,
            "release_date": item.release_date,
            "rating": item.rating,
            "review": item.review,
            "overview": item.overview,
            "movie_id": item.movie_id
        }
        movies_list.append(movie)
        id += 1
    return render_template("index.html", movies=movies_list)

@app.route("/delete")
def delete():
    url = request.url
    movie_id = url.split("=")[1]
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = Edit_movie()
    if form.validate_on_submit():
        url = request.url
        movie_id = url.split("=")[1]
        movie = Movie.query.get(movie_id)
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = Add_movie()
    if form.validate_on_submit():
        new_movie = Movie(movie_name=form.movie_name.data, release_date=form.release_date.data, rating=form.rating.data, review=form.review.data, overview=form.overview.data)
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
    
    