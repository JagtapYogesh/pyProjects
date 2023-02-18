from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret key'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location = StringField(label='Location Link', validators=[DataRequired()])
    open = StringField(label='Open', validators=[DataRequired()])
    close = StringField(label='Close', validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee', choices=['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'])
    wifi_rating = SelectField(label='Wifi', choices=['❎', '📶', '📶📶', '📶📶📶', '📶📶📶📶', '📶📶📶📶📶'])
    power_rating = SelectField(label='Power', choices=['❎', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'])
    submit = SubmitField(label='Add Cafe')

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode='a', encoding="utf8") as csv_file:
            csv_file.write(f"\n{form.cafe.data},{form.location.data},{form.open.data},{form.close.data},{form.coffee_rating.data},{form.wifi_rating.data},{form.power_rating.data}")
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
