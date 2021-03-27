"""Script to seed database."""

import os
import json
from random import choice, randint
import re  # this is to help split by two delimiters
import crud

# UNCOMMENT THESE 6 LINES IF YOU WANT TO SEED DATABASE
# import model
# import server
# os.system('dropdb yoga')
# os.system('createdb yoga')
# model.connect_to_db(server.app)
# model.db.create_all()

# Populate Poses DATA table (2 Columns, 2 Parameters, PK in API)
with open('data/rebecca.json') as rebecca:
    rebecca_data = json.loads(rebecca.read())

for pose in rebecca_data:
    current_pose = crud.create_pose(english_name=pose['english_name'],
                                    sanskrit_name=pose['sanskit_name'],
                                    img_url=pose['img_url']
                                    )

