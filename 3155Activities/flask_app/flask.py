# FLASK Tutorial 1 -- We show the bare bones code to get an app up and running

# imports
from flask import Flask   # Flask is the web app that we will customize

app = Flask(__name__)     # create an app

# @app.route is a decorator. It gives the function "index" special powers.
# In this case it makes it so anyone going to "your-url/" makes this function
# get called. What it returns is what is shown as the web page
@app.route('/index')
def index():
    return 'Welcome, Notes App User!'

