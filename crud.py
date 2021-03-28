"""CRUD operations."""

from model import *
# db, User, Pose, Sequence, SequenceStep, SavedSequence, SavedPose, connect_to_db

####################################CREATE##########################################

#/api/user-create
def create_user(first_name,
                last_name,
                email,
                user_level,
                password_hash):
    """ Creates a new user """

    user = User(first_name=first_name,
                last_name=last_name,
                email=email,
                user_level=user_level,
                password_hash=password_hash)

    db.session.add(user)
    db.session.commit()

    return user

#seed.py, not in routes
def create_pose(english_name,
                sanskrit_name,
                img_url,
                pose_level):
                # instructions,
                # video_url):
    """ Creates a new pose """

    pose = Pose(english_name=english_name,
                sanskrit_name=sanskrit_name,
                img_url=img_url,
                pose_level=pose_level)
                # instructions=instructions,
                # video_url=video_url)

    db.session.add(pose)
    db.session.commit()

    return pose

#api/create-sequence
def create_sequence(seq_name, seq_level):
    """ Creates a new sequence """

    sequence = Sequence(seq_name=seq_name,
                        seq_level=seq_level)

    db.session.add(sequence)
    db.session.commit()

    return sequence

#api/create-sequence
def create_sequence_step(step_num, pose_id, seq_id):
    """ Creates a sequence step """

    sequence_step = SequenceStep(step_num=step_num,

                                pose_id=pose_id,
                                seq_id=seq_id)

    db.session.add(sequence_step)
    db.session.commit()

    return sequence_step


def create_saved_sequence(seq_id, user_id, completed):

    saved_sequence = SavedSequence (seq_id=seq_id, 
                                    user_id=user_id,
                                    completed=completed)

    db.session.add(saved_sequence)
    db.session.commit()

    return saved_sequence                            


def create_saved_pose(pose_id, user_id):
    """ Creates a saved se. """

    saved_pose = SavedPose(
        pose_id=pose_id, user_id=user_id)

    db.session.add(saved_pose)
    db.session.commit()

    return saved_pose


####################################READ##########################################


def get_all_users():
    """Return all users."""

    return User.query.all()
    
def get_user_by_id(user_id):
    """Return a user by user ID."""

    return User.query.filter(User.user_id == user_id).first()

#/api/user-create
#/login
def get_user_by_email(email):
    """ Returns a user by their email. """

    return User.query.filter(User.email == email).first()

def get_all_poses():
    """ Returns all poses """

    return Pose.query.all()

def get_pose_by_id(pose_id):
    """Return one pose. """

    return Pose.query.filter_by(pose_id=pose_id).one()

def get_pose_by_name_eng(english_name):
    """Return pose by English name. """

    return Pose.query.filter(Pose.english_name == english_name).first()
    # return Pose.query.filter_by(Pose.english_name == english_name).first()

def get_pose_by_name_sanskrit(sanskrit_name):
    """ Return a pose by Sanskrit name. """

    return Pose.query.filter(Pose.sanskrit_name == sanskrit_name).first()

def get_pose_by_level(pose_level):
    """ Returns all poses of a certain level. """

    return Pose.query.filter(Pose.pose_level == pose_level).all()

def get_sequence_by_name(seq_name):
    """ Return a sequence by name. """
    return SavedSequence.query.filter(SavedSequence.seq_name == seq_name).first()

def get_sequence_by_level(seq_level):
    """ Returns all sequences of a certain level. """

    return Sequence.query.filter(Sequence.seq_level == seq_level).all()

def get_users_sequences(user_id):
    """Input user_id, return query of all user's saved sequences."""
    return SavedSequence.query.filter(SavedSequence.user_id == user_id).all()

def get_steps_by_sequence(seq_id):
    """ Returns all steps from a sequence """

    return SequenceStep.query.filter(SequenceStep.seq_id == seq_id).all()



####################################UPDATE##########################################

def update_user(user_id, first_name=None, last_name=None, new_email=None):
    """Update user and return user."""
    
    user = db.session.query(User).get(user_id)

    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name
    if new_email:
        user.email = new_email

    db.session.commit()

    return user


####################################DELETE##########################################

def delete_user(user_id):
    """Deletes user"""

    user = db.session.query(User).get(user_id)

    db.session.delete(user)
    db.session.commit()

    return f'User {user_id} is deleted.'


def delete_user_sequence(user_id, seq_id):
    """Given user_id and seq_id, deletes a saved sequence from database."""
    
    unwanted_sequence = SavedSequence.query.filter(
                                                SavedSequence.user_id == user_id, 
                                                SavedSequence.seq_id == seq_id).one()
    db.session.delete(unwanted_sequence)
    db.session.commit() 




#RACHEL'S SEARCH FEATURE
# def search_poses(search_phrase):
#     """Searches poses based on the input phrase and returns pose_name."""

#     related_recipes_id = set()
#     search = "%{}%".format(search_phrase).lower()

#     tag_results = Tag.query.filter(Tag.name.ilike(search)).all()
#     # print("Tag Results", tag_results)
#     for tag in tag_results:
#         tag_recipes = get_recipe_ids_by_tag_id(tag.tag_id)
#         for recipe in tag_recipes:
#             related_recipes_id.add(recipe)
#     # print("These are all the related recipe ids:", related_recipes_id)

#     ingredients_results = Ingredient.query.filter(Ingredient.detailed_ingredient.ilike(search)).all()
#     # print("Ingredients Results", ingredients_results)
#     for ingredient in ingredients_results:
#         related_recipes_id.add(ingredient.recipe_id) 
#     # print("These are all the searches including ingredients as well!", related_recipes_id)

#     title_results = Recipe.query.filter(Recipe.title.ilike(search)).all()
#     # print("Recipe Title Results", title_results)
#     for recipe in title_results:
#         related_recipes_id.add(recipe.recipe_id) 

#     print("These are all the searches including Title results as well!", related_recipes_id)

#     return related_recipes_id


def get_creators_info():
    pass




if __name__ == '__main__':
    from server import app
    connect_to_db(app)
