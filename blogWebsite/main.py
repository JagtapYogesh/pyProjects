from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from datetime import datetime
import smtplib
from forms import CreatePostForm, EditPostForm, RegisterUserForm, ContactForm, LoginUserForm, CommentForm
from random import randint
MY_EMAIL = "jagtapyogesh324@gmail.com"
PASSWORD = "your password"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    user_id = db.Column(db.String(250), nullable=False)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    comment = db.Column(db.String(250), nullable=False)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, nullable=False)
    user_type = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/add", methods=['GET', 'POST'])
def add_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        todays_date = datetime.today().strftime('%Y-%m-%d')
        new_post = BlogPost(title=form.title.data,user_id=current_user.user_id, subtitle=form.subtitle.data, author=form.author.data, img_url=form.img_url.data, body=form.body.data, date=todays_date)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=form)

@app.route("/contact", methods=['GET', 'POST'])
@login_required
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:Message from {form.name.data}!\n\nUser with {form.email.data} and phone number {form.phone_no.data} has sent you message '{form.message.data}'")
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=form.email.data, msg=f"Subject:Message received!!!\n\nHi {form.name.data},\nYour message has been received. Will revert back to you shortly.\nThanks & Regards,\nYogesh\n\n If you did not send a message then please ignore this mail.")
            return render_template("info.html")
    return render_template("contact.html", form=form)

@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post = BlogPost.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/edit/<int:post_id>", methods=['GET', 'POST'])
def edit_post(post_id):
    form = EditPostForm()
    if form.validate_on_submit():
        post = BlogPost.query.get(post_id)
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.author = form.author.data
        post.img_url = form.img_url.data
        post.body = form.body.data
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=form)

@app.route('/home')
def get_all_posts():
    if current_user.user_type == "Reader":
        posts = BlogPost.query.all()
    else:
        posts = BlogPost.query.filter_by(user_id=current_user.user_id).all()
    return render_template("index.html", all_posts=posts, user_type=current_user.user_type)



@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginUserForm()
    if form.validate_on_submit():
        user_type = form.user_type.data
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user:
            if user.user_type == user_type:
                if check_password_hash(user.password, password):
                    login_user(user)
                    return redirect(url_for("get_all_posts"))
                else:
                    flash("Incorrect password. Please try again.")
            else:
                flash(f"You are a {user.user_type}. Please select the correct User type")
        else:
            flash("Email is not registered. Please register the email.")
    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/post/<int:index>", methods=['GET', 'POST'])
@login_required
def show_post(index):
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comment(post_id=index, date=datetime.today().strftime('%Y-%m-%d'), comment=form.comment.data, username=current_user.username)
        db.session.add(new_comment)
        db.session.commit()
    requested_post = BlogPost.query.get(index)
    comments = Comment.query.filter_by(post_id=index).all()
    return render_template("post.html", post=requested_post, form=form, comments=comments, user_type=current_user.user_type)






@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterUserForm()
    if form.validate_on_submit():
        user_type = form.user_type.data
        username = form.username.data
        email = form.email.data
        password = form.password.data
        user_id = f"{username[:2]}{randint(1,1000)}"
        new_user = User(username=username, email=email, user_id=user_id, user_type=user_type, password=generate_password_hash(password, method="pbkdf2:sha256", salt_length=8))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("register.html", form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)