<h1>How to Run the Web App</h1>

Steps:
1. Install all the required libraries using the requirements.txt file. Best if it's under a virtual environment like venv etc.
2. This code was tested using Python 3.8

3. First we need to initialize the SQLite Database on the local computer.
4. Run the following commands in Terminal.
    > a. export FLASK_APP=app.py
    > b. flask db init
    > c. flask db migrate -m 'added migration'
    > d. flask db upgrade

5. Run the command in the terminal to run the experimental webserver
    python app.py

We should be able to access our website from localhost or http://127.0.0.1:5000. But we might need to do some IP and Port binding before we serve it to the public.


Disclaimer:
Although it's an experimental server and should not be used for production, but I thing for our BPG Project, we're not expecting heavy traffic. Otherwise we could use production grade server like Gunicorn etc.