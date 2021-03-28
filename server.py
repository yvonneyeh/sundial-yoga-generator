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

    return app.senatic_file('create-react-app')

    # after we are ready to deploy, we will make static files from our

# 3# @app.route('/api/recipes')

@app.route('/api/poses')
def all_pose_data():
  """Show all poses."""
  pass
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

@app.route('/api/poses/')
def show_poses_json():
  """Show all poses as JSON to use."""
  
  poses = crud.get_all_poses() 
  pose_data = poses.serialize

  serialized_pose_data = [i.serialize for i in pose_data]

  return jsonify(serialized_pose_data)

@app.route('/api/creators/')
def show_creators_json():
  """Show creators information as JSON to use."""
  
  # Can we return this with creators.json directly somehow?
  # then we won't have to serialize?
  # and won't have to crud function it?

  with open('data/creators.json') as creators:
    creators_data = json.loads(creators.read())
  
  serialized_creators_data = [i.serialize for i in creators_data]

  return jsonify(serialized_creators_data)

@app.route('/api/poses/<pose_id>')
def pose_by_name_data(english_name=None, sanskrit_name=None):
  """Show all information of one pose."""

  english_name = crud.get_pose_by_name_english
  sanskrit_name = crud.get_pose_by_name_sanskrit

  pose_name = request.form.get('pose_name')

  # if given name is found in db, return the pose info


  # old code ...
  # pose_by_id = crud.get_pose_by_id(pose_id)
  # serialized_pose_data = pose_by_id.serialize

  # return jsonify(serialized_pose_data)
  # # The default is 24, you can change this parameter
  # pose_data = users_poses()

  # serialized_pose_data = [i.serialize for i in pose_data]

  # return jsonify(serialized_pose_data)




if __name__ == '__main__':
  connect_to_db(app)
  app.run(host='0.0.0.0', debug=True)