# Importing necessary libraries

import os
from forms import InfoForm
from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from time import gmtime, strftime
from datetime import datetime



# Initiating the Flask app, DB via SQLite and Config files
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config["SECRET_KEY"] = 'bpg_smartbox_team'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app) # passing the Flask App to database

#Setting up DB Migration
Migrate(app, db)


# Setting up the Database model/table
class UserFeedback(db.Model):

    __tablename__ = "feedbacks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    message = db.Column(db.Text)
    date_time = db.Column(db.Text)

    def __init__(self, name, email, message, date_time):
        # super().__init__()
        self.name = name
        self.email = email
        self.message = message
        self.date_time = date_time

    def __repr__(self) -> str:
        # return super().__repr__()
        return f'ID {self.id}: Name: {self.name}, Email: {self.email}, Feedback: {self.message} at {self.date_time}'

    
# HomePage of the website where we'll showcase our product
@app.route("/")
def index():
    return render_template("product_details.html")


# Page for users to submit their feedbacks
@app.route("/feedback", methods=['POST', 'GET'])
def feedback():

    form = InfoForm()

    if form.validate_on_submit():
        name = form.name.data
        email = "NO Email provided" if len(form.email.data) <= 0 else form.email.data
        message = form.message.data
        date_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        day = datetime.today().strftime('%A')
        day_date_time = str(day) + ", " + str(date_time)

        # Adding feedback and information to the Database
        add_new_feedback = UserFeedback(name, email, message, day_date_time)
        db.session.add(add_new_feedback)
        db.session.commit()

        flash(f"Feedback submitted. Thank you!")
        return redirect(url_for('show_feedback'))

    return render_template("feeback.html", form=form)


# Page to show all the users feedback
@app.route("/show_feedback", methods=['GET', 'POST'])
def show_feedback():
    all_feedbacks = False
    all_feedbacks = UserFeedback.query.all()

    return render_template("show_feedback.html", all_feedbacks=all_feedbacks)



# Custom error handler page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404


# Running the app
if __name__ == "__main__":
    app.run(debug=True)