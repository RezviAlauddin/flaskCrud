from flask import Flask, app
from modulefinder import*

from flask.templating import render_template
from dotenv import load_dotenv

load_dotenv('.flaskenv')

app = Flask(__name__)

@app.route('/')
def index(methods=['GET','POST'] ):
    return render_template('index.html')
