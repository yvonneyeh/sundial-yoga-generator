"""Server for HackOR app"""

import os
from flask import (Flask, render_template, request,
                   flash, session, redirect, jsonify)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined
import json
import markov

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

    return app.send_static_file('home.html')

    # after we are ready to deploy, we will make static files from our

# 3# @app.route('/api/recipes')

# @app.route('/api/poses')
# def all_pose_data():
#   """Show all poses."""
#   pass
# poses  # poses_datais 24, you can change this parameter
#   recipe_data poses as JSON to useget_recipes()

#   serialized_recipe_data = [i.serialize for i in recipe_data]

# pose_dataget_poses return jsonify(serialized_recipe_data)aweserializeaweserialized_recipe_dataposepose_datapose@app.route('/api/poses')

# @app.route('/api/user-create', method=['POST'])
# def create_new_user():
#   """Create user account."""


#   first_name = request.form.get('first_name')
#   last_name = request.form.get('last_name')
#   email = request.form.get('email')
#   user_level = request.form.get('user_level')
#   password_hash = generate_password_hash(request.form.get('password'))


#   user = crud.get_user_by_email(email)

#   if user:
#     response = {
#       "errorMessage": "This email is already associated to an account. Try logging in.",
#       "image": "https://http.cat/409",
#     }
#     status = 409
#     print(response.errorMessage)
#     print(jsonify(response), status)

#     return jsonify(response), status

#   else:
#     userCreated = crud.create_user(first_name, last_name, email, user_level, password_hash)
#     userAccountMade = crud.get_user_by_email(email)

#     response = {
#       "errorMessage": "None.",
#       "image": "https://http.cat/409.jpg",
#       "user": userAccountMade.serialize
#     }
#     status = 200

#     print("You made a yoga account!", jsonify(response), status)

#     return jsonify(response), status

# @app.route('/login', methods=['POST'])
# def login():

#     email = request.form.get('email')
#     password = request.form.get('password')

#     user_obj = crud.get_user_by_email(email)

#     if user_obj != None:
#         if password == user_obj.password:
#             session['user_id'] = user_obj.user_id
#             return redirect('/profile.html')
#         else:
#             flash('Incorrect password, please try again')
#     else:
#         flash('You have not created an account with that email. Please create account')
#     return redirect('/')


# @app.route('/api/create-sequence', method=['POST'])
# def create_sequence():
#   """Create sequence."""

#   seq_name = request.form.get('seq_name')
#   seq_level = request.form.get('seq_level')
#   seq_length = request.form.get('seq_length')

#   seq_made = crud.create_sequence(seq_name, seq_level)

#   seq_made.sequence_id

#   # seq_level = number of steps

# @app.route('/get-callback-info', methods=["POST"])
# def get_callback_info():
#     if 'user_id' in session:
#         user_id = session['user_id']
#         project_id = request.json.get('project_id')
#         callback_info = crud.get_projects_by_user_and_project_id(user_id, project_id)
#         callback_dict = callback_info.__dict__
#         callback_dict.pop('_sa_instance_state')

#         return jsonify(callback_dict)


@app.route('/api/poses/')
def show_poses_json():
    """Show all poses as JSON to use."""

    poses = crud.get_all_poses()

    jsonlist = [i.serialize for i in poses]

    return jsonify(jsonlist)


@app.route('/api/creators/')
def show_creators_json():
    """Show creators information as JSON to use."""

    creators_data = crud.get_all_creators()

    print("*****\n****\n******\n******\n***")
    print(creators_data) # output: []

    # jsonlist = [i.serialize for i in creators_data]

    # return jsonify(jsonlist)


@app.route('/api/user/<user_id>')
def user_info(user_id):
    """Show the user's info by id."""
    user = crud.get_user_by_id()

    json_me = [user.serialize]

    return jsonify(json_me)
    # old code ...
    # pose_by_id = crud.get_pose_by_id(pose_id)
    # serialized_pose_data = pose_by_id.serialize

    # return jsonify(serialized_pose_data)
    # # The default is 24, you can change this parameter
    # pose_data = users_poses()

    # serialized_pose_data = [i.serialize for i in pose_data]

    # return jsonify(serialized_pose_data)


@app.route('/api/random-sequence/')
def get_random_sequence():
    """Create long, 45-70 minute sequence."""

    sequence = markov.create_long_sequence()

    # jsonlist = [i.serialize for i in sequence]

    # return jsonify(jsonlist)
    return jsonify(sequence)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
