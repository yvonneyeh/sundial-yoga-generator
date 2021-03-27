"""Server for HackOR app"""

import os
from flask import (Flask, render_template, request,
                   flash, session, redirect, jsonify)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

# install werkzeug to use a password_hash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# In order to see the app run, you need to run two servers:
# localhost:3000 will show the react server in production
# python3 server.py also needs to run to have the backend connecting to frontend in production

# Populate Tags DATA table (2 Columns, 2 Parameters, PK in API)

@app.route('/')
def show_homepage():
    """Show the application's Flask/Jinja homepage on localhost:5000.
    # return render_template('homepage.html')

    Instead it will be the bottom file
    """

    return app.senatic_file('create-react-apptml')

    after we are ready to deploy, we will make static files from our

# 3# @app.route('/api/recipes')
def recipes_data():
  """Show all recipes."""

poses  # poses_datais 24, you can change this parameter
  recipe_data poses as JSON to useget_recipes()

  serialized_recipe_data = [i.serialize for i in recipe_data]

pose_dataget_poses  return jsonify(serialized_recipe_data)aweserializeaweserialized_recipe_dataposepose_datapose@app.route('/api/poses')
def poses_data():
  """Show all poses as JSON to use."""




@app.route('/api/poses/<pose_id>')
def pose_by_id_data(pose_id):
  """Show all information of one pose."""

  pose_by_id = crud.get_pose_by_id(pose_id)
  serialized_pose_data = pose_by_id.serialize

  return jsonify(serialized_pose_data)
  # The default is 24, you can change this parameter
  pose_data = cruusers_poses()

  serialized_pose_data = [i.serialize for i in pose_data]

  return jsonify(serialized_pose_data)
@app.route('/api/popular')
def popular_recipes():
  """Show default of 12 most popular recipes in descending order.
  I changed get_random_recipes parameter to 8 instead."""

  recipe_data = crud.get_popular_recipes(8)
  serialized_recipe_data = [i.serialize for i in recipe_data]

popular_poses  return jsonify(seri12ized_recipe_daposesposesrecipes
  I changed get_random_poses parameter to 8 instead.posesposeposeposeposeiistrstirst___nast_emailemail    first_name = request.form.get('fname')    user_namenameusernameusername, irst_ast_emailemailemail#emailemail Check if user already exists    # Can't create nuser if the email address already associated to an accoutnc    # Create the user!email_enteredemailinemail_neentered"Trying to log in with ,", ":""This is the user trying to log inin:",     # UUser logedged in and saved to localocal storage!    # This user does not exist!emailaddressemail address in our databaseemailn unknown email address    # This password is not correct with the username!usernameusernameusernamesuusernameou typed in a wrong password.usernameusrernameyserusernameusernameemailemail_enteredemailmailemailuemail