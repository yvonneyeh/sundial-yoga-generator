"""Script to seed database."""

import os
import json
from random import choice, randint
import re # this is to help split by two delimiters
import crud

# UNCOMMENT THIS IF YOU WANT TO SEED DATABASE
# import model
# import server

# os.system('dropdb recipes')
# os.system('createdb recipes')
# model.connect_to_db(server.app)
# model.db.create_all()