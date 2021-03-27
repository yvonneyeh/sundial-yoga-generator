"""Script to seed database."""

import os
import json
from random import choice, randint
from faker import Faker
import re  # this is to help split by two delimiters
import crud

# UNCOMMENT THESE 6 LINES IF YOU WANT TO SEED DATABASE
# import model
# import server
# os.system('dropdb yoga')
# os.system('createdb yoga')
# model.connect_to_db(server.app)
# model.db.create_all()

fake = Faker()

# Populate Poses DATA table (2 Columns, 2 Parameters, PK in API)
with open('data/rebecca.json') as rebecca:
    rebecca_data = json.loads(rebecca.read())

for pose in rebecca_data:
    current_pose = crud.create_pose(english_name=pose['english_name'],
                                    sanskrit_name=pose['sanskit_name'],
                                    img_url=pose['img_url']
                                    )

def load_json(filepath):
    with open(filepath) as data:
        json.loads(data.read())
    return read_data

poses_in_db = []
def seed_poses(read_data):
    for pose in read_data:
        if crud.get_pose_by_name_eng(english_name) == None:
            pose_obj = crud.create_pose(english_name=pose['english_name'],
                                    sanskrit_name=pose['sanskit_name'],
                                    img_url=pose['img_url']
                                    )
            poses_in_db.append(pose_obj)
    print(poses_in_db)


users_in_db = []
def seed_users():
    for n in range(20):
        email = f'yogi{n}@yoga.om'
        first_name = fake.first_name()
        last_name = fake.last_name()
        password_hash = 'test'
        level = 'intermediate'
        new_user = crud.create_user(first_name,last_name,email,password_hash,level)
        users_in_db.append(new_user)
    print(users_in_db)

#---------------------------------------------------------------------#

read_data = load_json('data/rebecca.json')
seed_poses(read_data)
