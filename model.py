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
    seq_name = db.Column(db.String, unique=True)

    def __repr__(self):
        return f'<User seq_id={self.seq_id} name={self.seq_name}>'


class SequenceStep(db.Model):
    """A step in a sequence."""

    __tablename__ = "steps"

    step_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    step_num = db.Column(db.Integer)
    pose_id = db.Column(db.Integer, db.ForeignKey('poses.pose_id'))
    seq_id = db.Column(db.Integer, db.ForeignKey('sequences.seq_id'))

    def __repr__(self):
        return f'<Step #{self.step_num} of Sequence #{self.seq_id} >'


class SavedSequence(db.Model):
    """A step in a sequence."""

    __tablename__ = "saved_sequences"

    step_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    step_num = db.Column(db.Integer)
    pose_id = db.Column(db.Integer, db.ForeignKey('poses.pose_id'))
    seq_id = db.Column(db.Integer, db.ForeignKey('sequences.seq_id'))

    def __repr__(self):
        return f'<Step #{self.step_num} of Sequence #{self.seq_id} >'


class UserPose(db.Model):
    """A step in a sequence."""

    __tablename__ = "user_poses"

    pose_id = db.Column(db.Integer, db.ForeignKey('poses.pose_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    saved = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<pose_id={self.pose_id} saved by user_id={self.user_id} >'


# class PoseCategory(db.Model):
#     pass
