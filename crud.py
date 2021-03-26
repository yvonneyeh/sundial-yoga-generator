"""CRUD operations."""

from model import db, User, Pose, Category, Sequence, SequenceStep, SavedSequence, UserProse, PoseCategory, connect_to_db


def create_user(username,
                first_name,
                last_name,
                email,
                password):
    """ Creates a new user """

    user = User(username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password)

    db.session.add(user)
    db.session.commit()

    return user


def create_pose(english_name,
                sanskrit_name,
                instructions,
                img_url,
                video_url):
    """ Creates a new pose """

    pose = Pose(english_name=english_name,
                sanskrit_name=sanskrit_name,
                instructions=instructions,
                img_url=img_url,
                video_url=video_url)

    db.session.add(pose)
    db.session.commit()

    return pose


def create_category():
    pass


def create_sequence():
    pass


def create_sequence_step():
    pass


def create_saved_sequence():
    pass


def create_user_pose():
    pass


def creat_pose_category():
    pass
if __name__ == '__main__':
    from server import app
    connect_to_db(app)