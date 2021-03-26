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


