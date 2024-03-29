# FLASK Tutorial 1 -- We show the bare bones code to get an app up and running

# imports
from flask import Flask   # Flask is the web app that we will customize
from flask import render_template
app = Flask(__name__)     # create an app

# @app.route is a decorator. It gives the function "index" special powers.
# In this case it makes it so anyone going to "your-url/" makes this function
# get called. What it returns is what is shown as the web page
@app.route('/index')
def index():
    a_user = {'name': 'Daniel House', 'email':'mogli@uncc.edu'}
    return render_template('index.html', user = a_user)

@app.route('/notes')
def get_notes():
    notes = { 1 : { 'title': 'First note' , 'text' : 'This is my first note' , 'date': '10-1-2020'},
              2 : { 'title': 'Second note' , 'text' : 'This is my second note' , 'date': '10-2-2020'},
              3 : { 'title': 'Third note' , 'text' : 'This is my third note' , 'date' : '10-3-2020'}
            }
    return render_template('notes.html', notes=notes)

@app.route('/note')
def get_note(note_id):
    notes = { 1 : { 'title': 'First note' , 'text' : 'This is my first note' , 'date': '10-1-2020'},
              2 : { 'title': 'Second note' , 'text' : 'This is my second note' , 'date': '10-2-2020'},
              3 : { 'title': 'Third note' , 'text' : 'This is my third note' , 'date' : '10-3-2020'}
            }
    return render_template('notes.html', notes=notes[int(note_id)])