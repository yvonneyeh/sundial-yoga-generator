"""Models for yoga sequencer app."""
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Creator(db.Model):
    """A user."""

    __tablename__ = "creators"

    name = db.Column(db.String(75), primary_key=True)
    img = db.Column(db.String(100))
    github = db.Column(db.String(70))
    linkedin = db.Column(db.String(70), unique=True)
    about = db.Column(db.String())

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'name': self.name,
            'img': self.img,
            'github': self.github,
            'linkedin': self.linkedin,
            'about': self.about
        }

    def __repr__(self):
        return f'<Creator={self.name} linkedin={self.linkedin}>'


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

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'user_id': self.user_id,
            'fist_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone,
            'password_hash': self.password_hash
        }

    def __repr__(self):
        return f'<User name={self.first_name} {self.last_name} email={self.email}>'


class Pose(db.Model):
    """A yoga pose."""

    __tablename__ = "poses"

    pose_id = db.Column(db.Integer, primary_key=True)
    english_name = db.Column(db.String(50))
    sanskrit_name = db.Column(db.String(60))
    instructions = db.Column(db.String(500))
    img_url = db.Column(db.String(200))
    video_url = db.Column(db.String(200))
    pose_level = db.Column(db.String(20))

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'pose_id': self.pose_id,
            'english_name': self.english_name,
            'sanskrit_name': self.sanskrit_name,
            'instructions': self.instructions,
            'img_url': self.img_url,
            'video_url': self.video_url,
            'pose_level': self.pose_level
        }

    def __repr__(self):
        return f'<Pose pose_id={self.pose_id} name={self.english_name}>'


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

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'seq_id': self.seq_id,
            'seq_name': self.seq_name,
            'seq_level': self.seq_level
        }

    def __repr__(self):
        return f'<User seq_id={self.seq_id} name={self.seq_name} level={self.seq_level}>'


class SequenceStep(db.Model):
    """A step in a sequence."""

    __tablename__ = "steps"

    step_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    step_num = db.Column(db.Integer)
    pose_id = db.Column(db.Integer, db.ForeignKey('poses.pose_id'))
    seq_id = db.Column(db.Integer, db.ForeignKey('sequences.seq_id'))

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'step_id': self.step_id,
            'step_num': self.step_num,
            'pose_id': self.pose_id,
            'seq_id': self.seq_id
        }

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

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'ss_id': self.ss_id,
            'seq_id': self.seq_id,
            'user_id': self.user_id,
            'completed': self.completed
        }

    # RELATIONSHIP
    user = db.relationship('User', backref=db.backref(
        'saved_sequences', order_by=seq_id))
    sequence = db.relationship('Sequence', backref=db.backref(
        'saved_sequences', order_by=seq_id))

    def __repr__(self):
        return f'<Saved sequence #{self.seq_id} by user {self.user_id} >'


class SavedPose(db.Model):
    """A user's saved sequence."""

    __tablename__ = "saved_poses"

    sp_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    pose_id = db.Column(db.Integer, db.ForeignKey('poses.pose_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'pose_id': self.pose_id,
            'user_id': self.user_id
        }

    # RELATIONSHIP
    user = db.relationship('User', backref=db.backref(
        'saved_poses', order_by=pose_id))
    pose = db.relationship('Pose', backref=db.backref(
        'saved_poses', order_by=pose_id))

    def __repr__(self):
        return f'<Pose #{self.pose_id} saved by user #{self.user_id} >'


# class PoseCategory(db.Model):
#     pass

##################################################


# How to connect my app to the DB
def connect_to_db(flask_app, db_uri=os.environ.get('DATABASE_URL') or 'postgresql:///yoga', echo=True):
    print("db_uri on model.py:", os.environ.get(
        'DATABASE_URL') or 'postgresql:///yoga')

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    db.app = flask_app
    db.init_app(flask_app)


if __name__ == '__main__':
    from server import app

    # rachel added these 3 lines 8:48 pm
    import os
    os.system('dropdb yoga')
    os.system('createdb yoga')

    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    connect_to_db(app)
    # Create tables if not already created. Delete all existing entries in tables.
    # db.create_all()

    print('Connected to db!')
