"""Server for HackOR app"""

import os
from flask import (Flask, render_template, request,
                   flash, session, redirect, jsonify)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# In order to see the app run, you need to run two servers:
# localhost:3000 will show the react server
# python3 server.py also needs to run to have the backend# Populate Tags DATA table (2 Columns, 2 Parameters, PK in API)
2@aa-rpp-route @app.route('/')def show_homepage():
    """Show the application's Flask/Jinja homepage on localhost:5000.
    # return render_template('homepage.html')
    - Changed this 3/9 to return next.js static index"""


    return app.senatic_file('create-react-apptml')

    after we are ready to deploy, we will make static files from our
    create-react-app files and this will render    