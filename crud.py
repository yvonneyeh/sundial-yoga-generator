"""CRUD operations."""

from model import db, User, Pose, Category, Sequence, SequenceStep, SavedSequence, UserPose, PoseCategory, connect_to_db


def create_user(first_name,
                last_name,
                email,
                password_hash):
    """ Creates a new user """

    user = User(first_name=first_name,
                last_name=last_name,
                email=email,
                password_hash=password_hash)

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


def create_sequence(seq_name):
    """ Creates a new sequence """

    sequence = Sequence(seq_name=seq_name)

    db.session.add(sequence)
    db.session.commit()

    return sequence


def create_sequence_step(step_num, pose_id, seq_id):
    """ Creates a sequence step """

    sequence_step = SequenceStep(step_num=step_num,
                                 pose_id=pose_id,
                                 seq_id=seq_id)

    db.session.add(sequence_step)
    db.session.commit()

    return sequence_step


def create_saved_sequence(step_num, pose_id, seq_id):
    """ Creates a saved sequence """

    saved_sequence = SavedSequence(step_num=step_num, pose_id=pose_id, seq_id=seq_id)


def create_user_pose(pose_id, user_id, saved):
    pass


# def create_pose_category():
#     pass


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
