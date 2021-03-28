"""Script to seed database."""

import os
import json
from random import choice, randint
from faker import Faker
# import re  # this is to help split by two delimiters
import crud
# import markov
import model
import server
# import pdb; pdb.set_trace()

fake = Faker()

# engine = create_engine('cockroachdb://root@localhost:26257/defaultdb?sslmode=disable')


def load_json(filepath):
    with open(filepath) as data:
        read_data = json.loads(data.read())
    return read_data


poses_in_db = []


def seed_poses(read_data):
    for pose in read_data:
        # if crud.get_pose_by_name_eng(pose) == None:
        pose_obj = crud.create_pose(english_name=pose['english_name'],
                                    sanskrit_name=pose['sanskrit_name'],
                                    img_url=pose['img_url'],
                                    pose_level=pose['pose_level']
                                    )
        poses_in_db.append(pose_obj)
    # print(poses_in_db)


users_in_db = []


def seed_users():
    for n in range(20):
        email = f'yogi{n}@yoga.om'
        first_name = fake.first_name()
        last_name = fake.last_name()
        password_hash = 'test'
        user_level = choice(['all', 'intermediate', 'advanced'])
        new_user = crud.create_user(
            first_name, last_name, email, password_hash, user_level)
        users_in_db.append(new_user)
    # print(users_in_db)


creators_in_db = []


def seed_creators():
    read_data = load_json('data/creators.json')
    print("\n\n\n\n", read_data, "\n\n\n\n")

    for creator in read_data:
        print("\n\n\n", creator, "\n\n\n")
        creator_obj = crud.create_creators(name=creator['name'],
                                           img=creator['img'],
                                           github=creator['github'],
                                           linkedin=creator['linkedin'],
                                           about=creator['about'])
        print("\n\n\n\n", creator_obj, "\n\n\n\n")
    creators_in_db.append(creator_obj)
    print("\n\n\n\n", creators_in_db, "\n\n\n\n")


seq_in_db = []


def seed_sequences():

    seq_name = "Power Yoga"
    level = choice(['all', 'intermediate', 'advanced'])
    new_sequence = crud.create_sequence(seq_name, level)
    seq_in_db.append(new_sequence)

    # print(seq_in_db)


steps_in_db = []


def seed_steps(sequence):

    for count, name in enumerate(sequence):
        step_num = count + 1
        pose_id = crud.get_pose_id_by_name(name)
        # test sequence ID
        seq_id = 1
        new_step = crud.create_sequence_step(step_num, pose_id, seq_id)
        steps_in_db.append(new_step)

    # print(steps_in_db)


#---------------------------------------------------------------------#
if __name__ == '__main__':



    # UNCOMMENT THESE LINES WHEN SEEDING DATABASE

    os.system('dropdb yoga')
    os.system('createdb yoga')

    model.connect_to_db(server.app)

    # Create tables if not already created. Delete all existing entries in tables.
    model.db.create_all()

    print("Tables created. Deleting all rows and creating new seed data.")
    # load_json('data/allposes.json')

    # Seed sample data into the database
    read_data = load_json('data/allposes.json')
    seed_poses(read_data)
    seed_users()
    seed_creators()
    seed_sequences()

    print("Sample data seeded")
