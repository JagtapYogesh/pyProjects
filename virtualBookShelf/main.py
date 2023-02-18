from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////books.db"

db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.String, nullable=False)


with app.app_context():
	db.create_all()




@app.route('/')
def home():
    all_books = Book.query.all()
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        bookname = request.form['bookname']
        bookauthor = request.form['bookauthor']
        rating = request.form['rating']
        new_book = Book(title=bookname, author=bookauthor, rating=rating)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    book = Book.query.get(id)
    if request.method == 'GET':
        book = Book.query.get(id)
        bookname= book.title
        rating = book.rating
        return render_template("update.html", book_name=bookname, rating=rating, id=book.id)
    if request.method == "POST":
        new_rating = request.form['newrating']
        book.rating     = new_rating
        db.session.commit()
        return redirect(url_for('home'))


@app.route("/deletebook/<int:id>")
def deletebook(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

