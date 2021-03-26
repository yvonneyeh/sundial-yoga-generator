"""Models for yoga sequencer app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    last_name = db.Column(db.String)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))

    def __repr__(self):
        return f'<User username={self.username} email={self.email}>'


class Pose(db.Model):
    """A yoga pose."""

    __tablename__ = "poses"

    pose_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    english_name = db.Column(db.String, unique=True)
    sanskrit_name = db.Column(db.String, unique=True)
    instructions = db.Column(db.String)
    img_url = db.Column(db.String)
    video_url = db.Column(db.String)

    def __repr__(self):
        return f'<User pose_id={self.pose_id} name={self.english_name}>'


class Category(db.Model):
    pass


class Sequence(db.Model):
    pass


class SequenceStep(db.Model):
    pass


class SavedSequence(db.Model):
    pass


class UserPose(db.Model):
    pass


class PoseCategory(db.Model):
    pass
