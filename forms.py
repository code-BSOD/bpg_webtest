from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField

# Setting up the form for receiving Feedbacks

class InfoForm(FlaskForm):
    name = StringField("Your Name: ")
    email = EmailField("Your Email")
    message = TextAreaField("Your Feedback")
    submit = SubmitField("Submit")