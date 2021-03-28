"""Models for yoga sequencer app."""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# unneeded I'm pretty sure, 
# app = Flask(__name__)


class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    # This is a security feature, password is being hashed
    password_hash = db.Column(db.String(120))
    user_level = db.Column(db.String(20))

    def __repr__(self):
        return f'<User username={self.username} email={self.email}>'


class Pose(db.Model):
    """A yoga pose."""

    __tablename__ = "poses"

    pose_id = db.Column(db.Integer, primary_key=True)
    english_name = db.Column(db.String(50), unique=True)
    sanskrit_name = db.Column(db.String(60), unique=True)
    instructions = db.Column(db.String(500))
    img_url = db.Column(db.String(200))
    video_url = db.Column(db.String(200))
    pose_level = db.Column(db.String(20))


    def __repr__(self):
        return f'<User pose_id={self.pose_id} name={self.english_name}>'


# class Category(db.Model):
#     """A category."""

#     __tablename__ = "categories"

#     category_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     category_name = db.Column(db.String, unique=True)

#     def __repr__(self):
#         return f'<User category_id={self.category_id} name={self.category_name}>'


class Sequence(db.Model):
    """A yoga sequence."""

    __tablename__ = "sequences"

    seq_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    seq_name = db.Column(db.String(100), unique=True)
    seq_level = db.Column(db.String(20))

    # RELATIONSHIPS
    # steps = a step in a sequence

    def __repr__(self):
        return f'<User seq_id={self.seq_id} name={self.seq_name}>'


class SequenceStep(db.Model):
    """A step in a sequence."""

    __tablename__ = "steps"

    step_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    step_num = db.Column(db.Integer)
    pose_id = db.Column(db.Integer, db.ForeignKey('poses.pose_id'))
    seq_id = db.Column(db.Integer, db.ForeignKey('sequences.seq_id'))

    # RELATIONSHIPS 
    sequence = db.relationship('Sequence', 
                                backref=db.backref('sequences',
                                order_by=step_num))
    pose = db.relationship('Pose', 
                                backref=db.backref('poses'))

    def __repr__(self):
        return f'<Step #{self.step_num} of Sequence #{self.seq_id} >'


class SavedSequence(db.Model):
    """A user's saved sequence."""

    __tablename__ = "saved_sequences"

    ss_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    seq_id = db.Column(db.Integer, db.ForeignKey('sequences.seq_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    completed = db.Column(db.Boolean, default=False)

    # RELATIONSHIP
    user = db.relationship('User', backref=db.backref('saved_sequences', order_by=seq_id))
    sequence = db.relationship('Sequence', backref=db.backref('saved_sequences', order_by=seq_id))

    def __repr__(self):
        return f'<Saved sequence #{self.seq_id} by user {self.user_id} >'


class SavedPose(db.Model):
    """A user's saved sequence."""

    __tablename__ = "saved_poses"

    sp_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    pose_id = db.Column(db.Integer, db.ForeignKey('poses.pose_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    
    # RELATIONSHIP
    user = db.relationship('User', backref=db.backref('saved_poses', order_by=pose_id))
    pose = db.relationship('Pose', backref=db.backref('saved_poses', order_by=pose_id))

    def __repr__(self):
        return f'<Pose #{self.pose_id} saved by user #{self.user_id} >'


# class PoseCategory(db.Model):
#     pass

##################################################


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///yoga'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.app = app
    db.init_app(app)

if __name__ == '__main__':
    from server import app

    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    connect_to_db(app)
    # Create tables if not already created. Delete all existing entries in tables.
    db.create_all()
    print('Connected to db!')