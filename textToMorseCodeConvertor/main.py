from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from data import Data

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = "dafadsfasdf83823@"
data = Data()
plain_text = ""
morse_code = ""


class PlainText(FlaskForm):
    text = TextAreaField(label="Enter your text:")
    submit_btn = SubmitField(label="Convert to Morse code")

@app.route("/", methods=['GET', 'POST'])
def home():
    form = PlainText()
    if form.validate_on_submit():
        global plain_text, morse_code
        morse_code = data.convert_text_to_code(form.text.data)
        plain_text = form.text.data
        return redirect(url_for('answer'))
    return render_template('index.html', form=form)


@app.route('/answer')
def answer():
    return render_template('answer.html', plain_text=plain_text, morse_code=morse_code)
if __name__ == "__main__":
    app.run(debug=True)